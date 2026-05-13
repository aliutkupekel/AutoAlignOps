import streamlit as st
import json
import os
from crewai import Crew, Task, Process

from agents.discovery import discovery_agent
from agents.optimizer import optimizer_agent
from agents.validator import validator_agent
from agents.deployer import deployer_agent
from mcp.registry_tools import ReadPromptTool, WritePromptTool
from mcp.probe_tools import ExecuteProbeTool

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AutoAlignOps Dashboard", page_icon="🤖", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(BASE_DIR, 'data', 'registry', 'prompts.json')

# --- DEVELOPER TOOLS (SIDEBAR - EN TEPEYE ALINDI KAYBOLMAYACAK) ---
st.sidebar.title("🛠️ Developer Tools")
if st.sidebar.button("🗑️ Clear Registry Archive", use_container_width=True):
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump({}, f)
    st.sidebar.success("Registry cleared!")
    st.rerun()

st.title("🚀 AutoAlignOps Multi-Agent Dashboard")
st.markdown("An AI agent team that automatically analyzes, optimizes, and safely deploys your LLM Prompts.")

def get_registry_data():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# --- SPLIT SCREEN INTO TWO COLUMNS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Your Inefficient Prompt")
    default_prompt = "You are a helpful assistant. Write a short summary. Not too long please."
    user_input_prompt = st.text_area("Enter the prompt you want to optimize:", value=default_prompt, height=200)
    
    st.markdown("---")
    st.subheader("📂 Deployment Registry (Archive)")
    st.json(get_registry_data())

with col2:
    st.subheader("⚙️ Operations Center")
    st.write("Click the button below to process your custom prompt.")
    
    if st.button("🔥 Optimize & Deploy This Prompt", use_container_width=True):
        if not user_input_prompt.strip():
            st.error("Please enter a prompt first!")
        else:
            with st.spinner("🤖 Agents are analyzing your input..."):
                
                read_tool = ReadPromptTool()
                write_tool = WritePromptTool()
                probe_tool = ExecuteProbeTool()

                task_discover = Task(
                    description=f"Analyze the following prompt provided by the user: '{user_input_prompt}'. Identify its inefficiencies, token bloat, and lack of constraints.",
                    expected_output="A detailed breakdown of the provided prompt's flaws.",
                    agent=discovery_agent
                )

                task_optimize = Task(
                    description="Based on the discovery report, rewrite the prompt using professional constraint framing and role clarity. Ensure the final prompt is plain text without complex markdown code blocks.",
                    expected_output="A completely rewritten, token-efficient prompt.",
                    agent=optimizer_agent
                )

                task_validate = Task(
                    description="Take the optimized prompt and execute behavioral probes using the 'execute_behavioral_probe' tool with suite_id 'custom_user_test'.",
                    expected_output="A formal mathematical report (BRR and P(A) metrics).",
                    agent=validator_agent,
                    tools=[probe_tool]
                )

                task_deploy = Task(
                    description="If validation is PASS (BRR == 0.0), save it to the registry with ID 'custom_prompt' and version 'v1.1'. Otherwise, report a rollback.",
                    expected_output="Deployment confirmation or rollback message.",
                    agent=deployer_agent,
                    tools=[write_tool]
                )

                crew = Crew(
                    agents=[discovery_agent, optimizer_agent, validator_agent, deployer_agent],
                    tasks=[task_discover, task_optimize, task_validate, task_deploy],
                    process=Process.sequential,
                    verbose=False
                )

                result = crew.kickoff()
                
                st.success("✅ Pipeline Execution Completed!")
                st.subheader("📊 Final Decision")
                st.info(str(result))

                st.subheader("🔄 Updated Registry Status")
                st.json(get_registry_data())