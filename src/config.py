import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
        Central configuration class for the Gemini AI Interviewer bot.

        This class handles environment variables, model parameters,
        and safety filters to ensure consistent behavior across the application.

        Attributes:
            API_KEY (str): The Google API key retrieved from environment variables.
            MODEL_NAME (str): The specific Gemini model identifier to be used.
            GENERATION_CONFIG (dict): Parameters to control the AI's response creativity
                and diversity (temperature, top_p, top_k).
            SAFETY_SETTINGS (dict): Thresholds for filtering potentially harmful content.
    """
    API_KEY = os.getenv("GEMINI_AI_KEY")
    MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")

    GENERATION_CONFIG = {
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 40
    }

    SAFETY_SETTINGS = {
        "HARASSMENT": "BLOCK_LOW_AND_ABOVE",
        "HATE": "BLOCK_LOW_AND_ABOVE",
        "SEXUAL": "BLOCK_LOW_AND_ABOVE",
        "DANGEROUS": "BLOCK_LOW_AND_ABOVE"
    }

    @staticmethod
    def validate_config():
        if not Config.API_KEY:
            raise ValueError("ERROR: The variable GEMINI_AI_KEY was not found in the .env file.")
        print(f"--- Settings loaded successfully (Template: {Config.MODEL_NAME}) ---")
