import google.generativeai as genai
import os

from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

API_KEY = os.getenv("GEMINI_AI_KEY")
genai.configure(api_key=API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods: # Verifica quais sáo os modelos para geração de conteúdo
        print(f"{m.name} - {m.description}")

# Confirguraçaão do agente
GENERATION_CONFIG = {
    "temperature": 0.5
}

# Configurações de segurança
SAFETY_SETTINGS = {
    "HARASSMENT": "BLOCK_LOW_AND_ABOVE",
    "HATE": "BLOCK_LOW_AND_ABOVE",
    "SEXUAL": "BLOCK_LOW_AND_ABOVE",
    "DANGEROUS": "BLOCK_LOW_AND_ABOVE"
}

# Inicializando IA
MODEL = genai.GenerativeModel(model_name="gemini-2.5-flash",
                              safety_settings=SAFETY_SETTINGS,
                              generation_config=GENERATION_CONFIG)

