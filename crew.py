from crewai import Crew,Process
from agents import blog_researcher,blog_writer,llmnew
from tasks import research_task,writing_task
# from tools import yt_tool


#Forming the crew that will generate the report
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
##Start the report generation tasks
# result = crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
# print(result)