@echo off
echo ========================================
echo Vishwakarma AI - Setup Script
echo (c) 2025 Vishwakarma Industries
echo ========================================
echo.

echo Step 1: Upgrading pip...
python -m pip install --upgrade pip
echo.

echo Step 2: Installing dependencies...
pip install -r requirements.txt
echo.

echo Step 3: Checking for .env file...
if not exist .env (
    echo .env file not found. Creating from .env.example...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file and add your API keys!
    echo - ELEVENLABS_API_KEY
    echo - NVIDIA_API_KEY
    echo.
    echo You can get API keys from:
    echo - ElevenLabs: https://elevenlabs.io/
    echo - NVIDIA: https://build.nvidia.com/
    echo.
) else (
    echo .env file already exists.
)

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your API keys
echo 2. Run: python run.py
echo.
echo For help, see API_SETUP.md
echo.
pause
