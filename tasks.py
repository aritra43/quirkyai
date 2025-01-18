from crewai import Task
from agents import blog_researcher,blog_writer,llmnew
# from tools import yt_tool

##Research Task

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