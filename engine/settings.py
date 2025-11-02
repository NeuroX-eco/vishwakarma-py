"""
Vishwakarma AI - Centralized Configuration
© 2025 Vishwakarma Industries

This file contains all the configuration settings for the application.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# General
ASSISTANT_NAME = "vishwakarma"
DATABASE_NAME = "vishwakarma.db"

# APIs
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_MODEL = "nvidia/llama2-70b"

# Paths
SAMPLES_PATH = 'engine/auth/samples'
TRAINER_PATH = 'engine/auth/trainer'
TRAINER_FILE = os.path.join(TRAINER_PATH, 'trainer.yml')
CASCADE_PATH = 'engine/auth/haarcascade_frontalface_default.xml'
