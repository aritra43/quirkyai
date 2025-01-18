from crewai import Agent
# from tools import yt_tool
# from dotenv import load_dotenv
from crewai import LLM
import litellm
import openai
import os
from crewai import Task
from crewai import Crew,Process
import streamlit

#Title 
streamlit.set_page_config(page_title="Quirky Liner",layout="wide")

#Title and description
streamlit.title("Quirky Liner Powered By CrewAI")
streamlit.markdown("Generates quirky lines based on personality")

#sidebar
with streamlit.sidebar:
    streamlit.header("Content Settings")

    characteristics1=streamlit.text_area(
        "Enter the first Characteristics",
        height=68,
        placeholder="Enter The First Characteristics",
        key="text_area_1"
    )
    # characteristics2=streamlit.text_area(
    #     "Enter the second Characteristics",
    #     height=68,
    #     placeholder="Enter The Second Characteristics",
    #     key="text_area_2"
    # )
    # characteristics3=streamlit.text_area(
    #     "Enter the third Characteristics",
    #     height=68,
    #     placeholder="Enter The Second Characteristics",
    #     key="text_area_3"
    # )
    
    streamlit.markdown("-----")

    generate_button=streamlit.button("Generate Content",type="primary",use_container_width=True )

def generate_content(characteristics1,blog="default"):
    
#     llmnew = LLM(
#     model="ollama/llama3.2", 
#     base_url="http://localhost:11434"
# )


##Create a senior blog content researcher

    blog_researcher = Agent(
        role='Content Researcher',
        goal='get the relevant catchy line that has to be printed on a shirt',
        name='Senior Content Researcher',
        description='a senior content writer that can write a catchy statement on the given characteristics {characteristics1}of a human ',
        verbose=True,
        memory=True,
        backstory=(
        "This is expert in writing a single catchy statement based on the given input characteristics {characteristics1} of a human"
        ),
        # tools=[yt_tool],
        llm= LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"
    ),
        allow_delegation=True,
    )

##Create a senior blog writer agent
    blog_writer = Agent(
        role='Content Writer',
        goal='Write a single catchy statement based on the given input characteristics {characteristics1} of a human that has to be printed on the shirt',
        description='A senior content writer that writes a catchy statement on the basis of the given input characteristics {characteristics1} of a human based on the research done by the content researcher agent',
        verbose=True,
        memory=True,
        backstory=(
        "This is a content writer that will write a catchy statement on the bisis of the given characteristics {characteristics1} of a human that has to be printed on a shirt"
        ),
        # tools=[yt_tool],
        llm= LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"
    ),
        allow_delegation=True,
    )

#Tasks
    research_task = Task(
        description=(
            "Search in the inetrnet and frame five great quality trippy single line catchy statemnt based on the given characteristics {characteristics1}  of the human"
        ),
        expected_output='Five great quality trippy single catchy statement based on the given input characteristics {characteristics1} of a human',
        # tools=[yt_tool],
        llm=LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"),
        agent=blog_researcher,
    )

    writing_task = Task(
        description=(
            "Write five great quality trippy different single line catchy statement that is mainly based on the given input characteristics {characteristics1} of a human"
        ),
        expected_output='Write five great quality trippy different single line catchy statement based on the given input characteristics {characteristics1} of a human',
        # tools=[yt_tool],
        llm=LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"),
        agent=blog_writer,
        async_execution=False,
        output_file='shirtdesign3.md',
    )

#Crew
    crew = Crew(
        agents=[blog_researcher,blog_writer],
        tasks=[research_task,writing_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True,
        # tools=[yt_tool],
        llm=LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"
    ),
)
# Function to get three inputs from the user
# def get_user_inputs():
#     characteristics1 = input("Enter the first characteristics: ")
#     characteristics2 = input("Enter the second characteristics: ")
#     characteristics3 = input("Enter the third characteristics: ")
#     return {
#         'characteristics1': characteristics1,
#         'characteristics2': characteristics2,
#         'characteristics3': characteristics3
#     }

# Main function to pass inputs to crew.kickoff
    # inputs={
    #     "characteristics1":characteristics1,
    # }
    return crew.kickoff(inputs={"characteristics1":characteristics1})

    # if __name__ = "__main__":
    #     return main()
    # Pass the inputs to crew.kickoff
    # result = crew.kickoff(inputs=user_inputs)
    # print("Result:", result)

if generate_button:
    with streamlit.spinner('Generating Content......This may take a moment.'):
        
        try:   
            result=generate_content(characteristics1,blog="Default blog content")
            streamlit.markdown("Generated Content")
            streamlit.markdown(result)
            topic="quirky"
            # streamlit.download_button(
            #     label="Download Content",
            #     data=result,
            #     file_name=f"{topic.lower().replace(' ','_')}_article.md",
            #     mime="text/markdown"
            # )
        except Exception as e:
            streamlit.error(f"An error occured:{str(e)}")

#Footer
streamlit.markdown("------")
streamlit.markdown("Made By CrewAI,Streamlit And Ollama")