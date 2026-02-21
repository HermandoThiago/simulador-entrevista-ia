import google.generativeai as genai

from src import Config

Config.validate_config()

genai.configure(api_key=Config.API_KEY)

model = genai.GenerativeModel(
    model_name=Config.MODEL_NAME,
    generation_config=Config.GENERATION_CONFIG,
    safety_settings=Config.SAFETY_SETTINGS
)