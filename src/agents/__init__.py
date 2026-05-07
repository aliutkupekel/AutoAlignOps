import os
import yaml
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

# .env dosyasındaki API bilgilerini yükle
load_dotenv()

def get_llm():
    """Groq API'sini OpenAI standartlarında LangChain üzerinden yükler."""
    return ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),
        model=os.getenv("MODEL_NAME"),
        temperature=0.2 # Matematiksel ve deterministik kalması için düşük sıcaklık
    )

def get_agent_config(agent_key):
    """YAML dosyasından ilgili ajanın rol, hedef ve hikayesini çeker."""
    config_path = os.path.join(os.path.dirname(__file__), '../../configs/agents_config.yaml')
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config[agent_key]