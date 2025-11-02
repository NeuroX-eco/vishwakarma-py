# 🔧 API Setup Guide - Vishwakarma AI

## Quick Start

### Step 1: Copy Environment File

```bash
copy .env.example .env
```

Or manually create a `.env` file in the project root directory.

### Step 2: Add Your API Keys

Open the `.env` file and replace the placeholder values with your actual API keys:

```env
ELEVENLABS_API_KEY=your_actual_elevenlabs_api_key_here
NVIDIA_API_KEY=your_actual_nvidia_api_key_here
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Required API Keys

### 1. ElevenLabs API (Text-to-Speech)

**Purpose**: High-quality voice synthesis for the assistant

**How to Get**:
1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up for a free account
3. Navigate to your Profile → API Keys
4. Copy your API key (starts with `sk_`)
5. Add to `.env` file:
   ```env
   ELEVENLABS_API_KEY=sk_your_key_here
   ```

**Free Tier**: 10,000 characters per month

**Fallback**: If not configured, the system will use Windows built-in TTS (pyttsx3)

---

### 2. NVIDIA AI API (Chatbot)

**Purpose**: AI-powered conversational responses

**How to Get**:
1. Visit [NVIDIA AI Foundation](https://build.nvidia.com/)
2. Sign up or log in with your NVIDIA account
3. Navigate to API Keys section
4. Generate a new API key (starts with `nvapi-`)
5. Add to `.env` file:
   ```env
   NVIDIA_API_KEY=nvapi-your_key_here
   ```

**Free Tier**: Limited requests per minute

**Fallback**: If not configured, the system will use basic pattern-matching responses

---

## ⚙️ Configuration Options

### Voice Settings

```env
# ElevenLabs Voice ID (default is Viraj - Male Hindi voice)
ELEVENLABS_VOICE_ID=iWNf11sz1GrUE4ppxTOL
```

To use a different voice:
1. Visit ElevenLabs Voice Library
2. Find a voice you like
3. Copy its Voice ID
4. Update the `.env` file

### AI Model Settings

```env
# NVIDIA AI Model (default is Llama 3.1 405B)
NVIDIA_MODEL=meta/llama-3.1-405b-instruct
```

**Available Models**:
- `meta/llama-3.1-405b-instruct` - Most capable (default)
- `meta/llama-3.1-70b-instruct` - Faster responses
- `mistralai/mixtral-8x7b-instruct` - Balanced performance

---

## 🔍 Troubleshooting

### Error: "ELEVENLABS_API_KEY is not set"

**Solution**:
1. Check if `.env` file exists in project root
2. Verify the API key is correctly formatted
3. Ensure no extra spaces around the `=` sign
4. Restart the application after updating `.env`

### Error: "NVIDIA API Error: 401 Unauthorized"

**Causes**:
- Invalid API key
- Expired API key
- API key not activated

**Solution**:
1. Verify your API key at [NVIDIA Build](https://build.nvidia.com/)
2. Generate a new API key if needed
3. Update `.env` file with the new key
4. Restart the application

### Error: "Rate limit exceeded (429)"

**Causes**:
- Too many requests in a short time
- Free tier limit reached

**Solution**:
1. Wait a few minutes before trying again
2. Consider upgrading your API plan
3. The system will automatically use fallback responses

### Error: "Connection timeout"

**Causes**:
- No internet connection
- Firewall blocking requests
- API service temporarily down

**Solution**:
1. Check your internet connection
2. Verify firewall settings
3. The system will automatically use fallback methods

---

## 🔒 Security Best Practices

### ✅ DO:
- Keep your `.env` file private
- Never commit `.env` to version control (already in `.gitignore`)
- Use different API keys for development and production
- Rotate API keys regularly
- Monitor API usage on provider dashboards

### ❌ DON'T:
- Share your API keys publicly
- Hardcode API keys in source code
- Commit `.env` file to Git
- Use production keys for testing
- Share screenshots containing API keys

---

## 📊 API Usage Monitoring

### ElevenLabs Dashboard
- Visit: https://elevenlabs.io/
- Check: Character usage, remaining quota
- Upgrade: If you need more characters

### NVIDIA Dashboard
- Visit: https://build.nvidia.com/
- Check: Request count, rate limits
- Upgrade: For higher limits

---

## 🆘 Getting Help

### API Key Issues
1. **ElevenLabs Support**: support@elevenlabs.io
2. **NVIDIA Support**: https://forums.developer.nvidia.com/

### Application Issues
1. Check `TROUBLESHOOTING.md` in the project
2. Review error messages in console
3. Verify all dependencies are installed

---

## 🎓 Testing Your Setup

### Test Script

Create a file `test_apis.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Test ElevenLabs API
elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
if elevenlabs_key and elevenlabs_key != "your_elevenlabs_api_key_here":
    print("✅ ElevenLabs API key is configured")
else:
    print("❌ ElevenLabs API key is NOT configured")

# Test NVIDIA API
nvidia_key = os.getenv("NVIDIA_API_KEY")
if nvidia_key and nvidia_key != "your_nvidia_api_key_here":
    print("✅ NVIDIA API key is configured")
else:
    print("❌ NVIDIA API key is NOT configured")
```

Run:
```bash
python test_apis.py
```

---

## 📝 Example .env File

```env
# API Keys
ELEVENLABS_API_KEY=sk_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz
ELEVENLABS_VOICE_ID=iWNf11sz1GrUE4ppxTOL

NVIDIA_API_KEY=nvapi-ABC123DEF456GHI789JKL012MNO345PQR678STU901VWX234YZ
NVIDIA_MODEL=meta/llama-3.1-405b-instruct

# Assistant Configuration
ASSISTANT_NAME=vishwakarma
COMPANY_NAME=Vishwakarma Industries
VERSION=1.0.0
```

---

## 🚀 Ready to Go!

Once you've configured your API keys:

1. Run the application:
   ```bash
   python run.py
   ```

2. The system will validate your API keys on startup
3. If keys are missing, fallback methods will be used automatically
4. Check the console for any configuration warnings

---

**Last Updated**: November 2, 2025  
**Version**: 1.0.0  
**© 2025 Vishwakarma Industries**
