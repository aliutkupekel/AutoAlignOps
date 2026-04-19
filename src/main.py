# src/main.py
from crewai import Crew, Task
from agents import create_agents
import mcp_server

def main():
    print("--- Starting AutoAlignOps Skeleton Project ---")
    
    # 1. MCP Server simülasyonunu test et
    mcp_server.read_registry("PROMPT-001")
    
    # 2. Ajanları yükle
    agents = create_agents()
    print(f"Successfully loaded {len(agents)} agents.")
    
    # 3. İskelet Görev (Task) Tanımla
    dummy_task = Task(
        description='Run a mock optimization cycle on PROMPT-001.',
        expected_output='A simulated success message confirming the pipeline works.',
        agent=agents[0] # Discovery agent ile başla
    )
    
    # 4. Crew'u kur (Ajanları birleştir)
    crew = Crew(
        agents=agents,
        tasks=[dummy_task],
        verbose=True
    )
    
    print("\n--- Architecture Baseline is Ready ---")
    print("All modules (Agents, MCP constraints) are properly linked.")

if __name__ == "__main__":
    main()