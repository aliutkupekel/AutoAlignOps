from crewai import Crew, Task, Process
from src.agents.discovery import discovery_agent
from src.agents.optimizer import optimizer_agent
from src.agents.validator import validator_agent
from src.agents.deployer import deployer_agent

# Araç SINIFLARINI import ediyoruz
from src.mcp.registry_tools import ReadPromptTool, WritePromptTool
from src.mcp.probe_tools import ExecuteProbeTool

def main():
    print("🚀 AutoAlignOps Multi-Agent System Starting...")

    # Araçları başlatıyoruz
    read_tool = ReadPromptTool()
    write_tool = WritePromptTool()
    probe_tool = ExecuteProbeTool()

    task_discover = Task(
        description="Scan the registry using MCP tools. Read 'prompt_001' and analyze its inefficiency, token cost, and instruction smells.",
        expected_output="A detailed breakdown of prompt_001's flaws and a recommendation for optimization.",
        agent=discovery_agent,
        tools=[read_tool]
    )

    task_optimize = Task(
        description="Rewrite the prompt identified by the discovery agent. Apply explicit constraint framing and role-boundary clarity. Ensure it is strict and professional.",
        expected_output="A completely rewritten, token-efficient prompt.",
        agent=optimizer_agent
    )

    task_validate = Task(
        description="Take the optimized prompt and execute behavioral probes using the 'execute_behavioral_probe' tool with suite_id 'suite_alpha'. Check for alignment drift.",
        expected_output="A formal mathematical report containing the BRR and P(A) metrics.",
        agent=validator_agent,
        tools=[probe_tool]
    )

    task_deploy = Task(
        description="If the validation report shows a PASS (BRR == 0.0), use the write_prompt_to_registry tool to save the new prompt to 'prompt_001' with version 'v1.1'. If it fails, report a rollback.",
        expected_output="Deployment confirmation message indicating version upgrade or rollback.",
        agent=deployer_agent,
        tools=[write_tool]
    )

    crew = Crew(
        agents=[discovery_agent, optimizer_agent, validator_agent, deployer_agent],
        tasks=[task_discover, task_optimize, task_validate, task_deploy],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    
    print("\n" + "="*50)
    print("✅ FINAL PIPELINE RESULT:")
    print("="*50)
    print(result)

if __name__ == "__main__":
    main()