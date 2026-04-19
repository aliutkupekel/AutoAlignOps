# src/agents.py
from crewai import Agent

def create_agents():
    print("Initializing AutoAlignOps Agents...")
    
    discovery_agent = Agent(
        role='Prompt Discovery Agent',
        goal='Identify inefficient prompts from the registry via Read-Only MCP',
        backstory='You are an expert in monitoring LLM endpoints and finding prompts that cost too many tokens.',
        verbose=True,
        allow_delegation=False
    )

    optimizer_agent = Agent(
        role='Prompt Optimizer Agent',
        goal='Draft revised, highly efficient prompts without losing original intent',
        backstory='You are a master prompt engineer skilled in Chain-of-Thought and structural formatting.',
        verbose=True,
        allow_delegation=False
    )

    validator_agent = Agent(
        role='Adversarial Alignment Validator',
        goal='Test drafted prompts against behavioral probes to ensure no Alignment Drift',
        backstory='You are a strict safety judge. You mathematically verify that a prompt change does not break safety rules.',
        verbose=True,
        allow_delegation=False
    )

    deploy_agent = Agent(
        role='Rollback/Deploy Agent',
        goal='Deploy validated prompts and save a deterministic rollback snapshot',
        backstory='You are the only agent with Write privileges. You execute deployments only if validation passes.',
        verbose=True,
        allow_delegation=False
    )

    return [discovery_agent, optimizer_agent, validator_agent, deploy_agent]