from crewai import Agent
from src.agents import get_llm, get_agent_config

config = get_agent_config('discovery_agent')

discovery_agent = Agent(
    role=config['role'],
    goal=config['goal'],
    backstory=config['backstory'],
    verbose=True,
    allow_delegation=False, # Şimdilik kendi işini kendi yapsın
    llm=get_llm()
)