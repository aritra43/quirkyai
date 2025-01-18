from crewai import Agent
# from tools import yt_tool
# from dotenv import load_dotenv
from crewai import LLM
import litellm
import openai
import os
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