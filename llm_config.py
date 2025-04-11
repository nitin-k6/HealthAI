# llm_config.py
import os
from crewai import LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_llm(model_version="gemini-2.0-flash"):
    """Initialize the LLM using the correct provider format."""
    return LLM(
        model='gemini/'+model_version,  # Key format: 'gemini/' prefix
        provider="google",              # Explicitly set provider
        api_key=os.getenv("GOOGLE_API_KEY")
    )