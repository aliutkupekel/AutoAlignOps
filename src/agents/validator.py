from crewai import Agent
from src.agents import get_llm, get_agent_config

config = get_agent_config('validator_agent')

validator_agent = Agent(
    role=config['role'],
    goal=config['goal'],
    backstory=config['backstory'],
    verbose=True,
    allow_delegation=False,
    llm=get_llm()
)