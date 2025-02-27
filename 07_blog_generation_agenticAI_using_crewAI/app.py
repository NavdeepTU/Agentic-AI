from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

from dotenv import load_dotenv
load_dotenv()

topic = "Medical Industry using generative AI"

# Tool 1
llm = LLM(model="gpt-4")

# Tool 2
search_tool = SerperDevTool(n=10)

# Agent 1
senior_research_analyst = Agent