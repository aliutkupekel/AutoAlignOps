import os
import json
from langchain.tools import tool
from src.mcp.schemas import ReadPromptSchema, WritePromptSchema

# Data yollarını dinamik olarak belirliyoruz
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
REGISTRY_PATH = os.path.join(BASE_DIR, 'data', 'registry', 'prompts.json')

def ensure_registry_exists():
    """Dosya yoksa boş bir JSON iskeleti oluşturur."""
    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    if not os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
            json.dump({}, f)

@tool("read_prompt_from_registry", args_schema=ReadPromptSchema)
def read_prompt_tool(prompt_id: str) -> str:
    """Reads a prompt's current content and metadata from the central registry."""
    ensure_registry_exists()
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    if prompt_id in registry:
        prompt_data = registry[prompt_id]
        return f"Content: {prompt_data['content']} | Version: {prompt_data['version']}"
    return f"Error: Prompt {prompt_id} not found."

@tool("write_prompt_to_registry", args_schema=WritePromptSchema)
def write_prompt_tool(prompt_id: str, new_content: str, version_tag: str) -> str:
    """Writes an optimized prompt to the registry, snapshotting the previous version."""
    ensure_registry_exists()
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    # Snapshot/Rollback mekanizması için eski versiyonu history'ye ekle
    if prompt_id in registry:
        old_data = registry[prompt_id].copy()
        history = registry[prompt_id].get("history", [])
        history.append({"version": old_data["version"], "content": old_data["content"]})
    else:
        history = []

    # Yeni veriyi kaydet
    registry[prompt_id] = {
        "content": new_content,
        "version": version_tag,
        "history": history
    }
    
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=4)
        
    return f"Success: Prompt {prompt_id} updated to version {version_tag}."