from crewai import Agent
# from tools import yt_tool
# from dotenv import load_dotenv
from crewai import LLM
import litellm
import openai
import os
from crewai import Task
from crewai import Crew,Process
# load_dotenv()

llmnew = LLM(
    model="ollama/llama3.2", 
    base_url="http://localhost:11434"
)


##Create a senior blog content researcher

blog_researcher = Agent(
    role='Content Researcher',
    goal='get the relevant catchy line that has to be printed on a shirt',
    name='Senior Content Researcher',
    description='a senior content writer that can write a catchy statement on the given characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human ',
    verbose=True,
    memory=True,
    backstory=(
     "This is expert in writing a single catchy statement based on the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human"
    ),
    # tools=[yt_tool],
    llm=llmnew,
    allow_delegation=True,
)

##Create a senior blog writer agent
blog_writer = Agent(
    role='Content Writer',
    goal='Write a single catchy statement based on the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human that has to be printed on the shirt',
    description='A senior content writer that writes a catchy statement on the basis of the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human based on the research done by the content researcher agent',
    verbose=True,
    memory=True,
    backstory=(
     "This is a content writer that will write a catchy statement on the bisis of the given characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human that has to be printed on a shirt"
    ),
    # tools=[yt_tool],
    llm=llmnew,
    allow_delegation=True,
)

#Tasks
research_task = Task(
    description=(
        "Search in the inetrnet and frame five great quality trippy single line catchy statemnt based on the given characteristics {characteristics1}, {characteristics2}, {characteristics3} of the human"
    ),
    expected_output='Five great quality trippy single catchy statement based on the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human',
    # tools=[yt_tool],
    llm=llmnew,
    agent=blog_researcher,
)

writing_task = Task(
    description=(
        "Write five great quality trippy different single line catchy statement that is mainly based on the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human"
    ),
    expected_output='Write five great quality trippy different single line catchy statement based on the given input characteristics {characteristics1}, {characteristics2}, {characteristics3} of a human',
    # tools=[yt_tool],
    llm=llmnew,
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
    llm=llmnew
)
# Function to get three inputs from the user
def get_user_inputs():
    characteristics1 = input("Enter the first characteristics: ")
    characteristics2 = input("Enter the second characteristics: ")
    characteristics3 = input("Enter the third characteristics: ")
    return {
        'characteristics1': characteristics1,
        'characteristics2': characteristics2,
        'characteristics3': characteristics3
    }

# Main function to pass inputs to crew.kickoff
def main():
    # Get user inputs
    user_inputs = get_user_inputs()
    
    # Pass the inputs to crew.kickoff
    result = crew.kickoff(inputs=user_inputs)
    print("Result:", result)

# Run the main function
if __name__ == "__main__":
    main()