"""
Vishwakarma AI - Configuration Module
© 2025 Vishwakarma Industries
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ASSISTANT_NAME = "vishwakarma"
COMPANY_NAME = "Vishwakarma Industries"
YEAR = 2025
VERSION = "1.0.0"

# API Keys - Load from environment variables with fallback values
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "iWNf11sz1GrUE4ppxTOL")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-405b-instruct")

# Validate API keys
def validate_api_keys():
    """Validate that required API keys are present"""
    errors = []
    
    if not ELEVENLABS_API_KEY:
        errors.append("ELEVENLABS_API_KEY is not set. Please add it to your .env file.")
    
    if not NVIDIA_API_KEY:
        errors.append("NVIDIA_API_KEY is not set. Please add it to your .env file.")
    
    return errors

# Check for API key errors on import
api_errors = validate_api_keys()
if api_errors:
    print("\n⚠️  API Configuration Warnings:")
    for error in api_errors:
        print(f"   - {error}")
    print("\nThe application will use fallback methods when APIs are unavailable.\n")