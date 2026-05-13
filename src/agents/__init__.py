import os
import yaml
from dotenv import load_dotenv
from crewai import LLM

# .env dosyasındaki API bilgilerini yükle
load_dotenv()

def get_llm():
    """Groq API'sini tamamen native CrewAI LLM sınıfı ile bağlar."""
    return LLM(
        model="groq/llama-3.3-70b-versatile", # 18 dakikalık cezamız bitti, kral geri döndü!
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.2
    )

def get_agent_config(agent_key):
    """YAML dosyasından ilgili ajanın rol, hedef ve hikayesini çeker."""
    config_path = os.path.join(os.path.dirname(__file__), '../../configs/agents_config.yaml')
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config[agent_key]