# 🔌 API Integration Guide

**© 2025 Vishwakarma Industries**

---

## 🎯 Overview

Vishwakarma AI now uses **premium APIs** for enhanced performance:

- **🎙️ ElevenLabs** - High-quality Text-to-Speech
- **🤖 NVIDIA AI** - Advanced Language Model

---

## ✅ What's Integrated

### **1. ElevenLabs TTS**

**API Key:** `sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58`  
**Voice:** Viraj (Male Hindi) - `iWNf11sz1GrUE4ppxTOL`

**Features:**
- ✅ Natural-sounding voice
- ✅ Hindi language support
- ✅ Professional quality
- ✅ Fast response time
- ✅ Automatic fallback to pyttsx3

**Location:** `engine/command.py` - `speak()` function

### **2. NVIDIA AI (LLM)**

**API Key:** `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`  
**Model:** Meta Llama 3.1 405B Instruct

**Features:**
- ✅ Advanced conversational AI
- ✅ Context-aware responses
- ✅ Fast inference
- ✅ Concise voice-optimized responses
- ✅ Automatic fallback to basic responses

**Location:** `engine/features.py` - `chatBot()` function

---

## 🚀 Quick Start

### **Installation**

```bash
# Install required packages
pip install openai requests

# Or install all requirements
pip install -r requirements.txt
```

### **Usage**

Just run Vishwakarma AI normally:

```bash
python run.py
```

**That's it!** The APIs are pre-configured and ready to use.

---

## 🔧 Configuration

### **API Keys Location**

File: `engine/config.py`

```python
# ElevenLabs TTS
ELEVENLABS_API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"
ELEVENLABS_VOICE_ID = "iWNf11sz1GrUE4ppxTOL"

# NVIDIA AI
NVIDIA_API_KEY = "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"
NVIDIA_MODEL = "meta/llama-3.1-405b-instruct"
```

### **Change Voice**

Edit `engine/config.py`:

```python
# Available voices:
ELEVENLABS_VOICE_ID = "iWNf11sz1GrUE4ppxTOL"  # Viraj - Male Hindi
# ELEVENLABS_VOICE_ID = "u7bRcYbD7visSINTyAT8"  # Male Voice
# ELEVENLABS_VOICE_ID = "NHRgOEwqx5WZNClv5sat"  # Female Voice 1
# ELEVENLABS_VOICE_ID = "jUjRbhZWoMK4aDciW36V"  # Female Voice 2
```

### **Change AI Model**

Edit `engine/config.py`:

```python
# Available models:
NVIDIA_MODEL = "meta/llama-3.1-405b-instruct"  # Current (Best)
# NVIDIA_MODEL = "openai/gpt-oss-120b"  # Alternative
# NVIDIA_MODEL = "mistralai/mixtral-8x7b-instruct"  # Faster
```

---

## 🎤 How TTS Works

### **Flow:**

1. Text received from `speak()` function
2. Send to ElevenLabs API
3. Receive audio (MP3)
4. Save to temp file
5. Play audio
6. Delete temp file

### **Fallback:**

If ElevenLabs fails:
- Automatically switches to pyttsx3
- No interruption in service
- Error logged to console

### **Code:**

```python
def speak(text):
    try:
        # Try ElevenLabs
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            # Play audio
            playsound(audio_file)
    except:
        # Fallback to pyttsx3
        fallback_speak(text)
```

---

## 🤖 How AI Works

### **Flow:**

1. User query received
2. Send to NVIDIA API with context
3. Receive AI response
4. Speak response using TTS

### **System Prompt:**

```
You are Vishwakarma AI, an intelligent voice assistant created by 
Vishwakarma Industries. You are helpful, friendly, and provide 
concise responses suitable for voice interaction.
```

### **Parameters:**

```python
temperature=0.7      # Balanced creativity
top_p=0.9           # Diverse responses
max_tokens=200      # Concise for voice
stream=False        # Complete response
```

### **Fallback:**

If NVIDIA API fails:
- Basic pattern-matching responses
- Time/date queries
- Greetings
- Identity questions

---

## 💰 API Costs & Limits

### **ElevenLabs**

**Free Tier:**
- 10,000 characters/month
- All voices included
- Standard quality

**Current Usage:**
- ~50-100 characters per response
- ~100-200 responses/month with free tier

**Monitoring:**
```python
# Check usage
response = requests.get(
    "https://api.elevenlabs.io/v1/user",
    headers={"xi-api-key": API_KEY}
)
```

### **NVIDIA AI**

**Free Tier:**
- Limited requests per minute
- Suitable for personal use
- No hard limit specified

**Rate Limiting:**
- Automatic retry on rate limit
- Fallback to basic responses
- No service interruption

---

## 🔒 Security

### **Current Setup:**

- ✅ API keys in config file
- ✅ Not exposed in UI
- ✅ Local execution only

### **Best Practices:**

**For Production:**

1. **Use Environment Variables:**
```python
import os
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY')
```

2. **Use .env File:**
```bash
# .env
ELEVENLABS_API_KEY=your_key_here
NVIDIA_API_KEY=your_key_here
```

3. **Add to .gitignore:**
```
.env
config.py
```

---

## 🧪 Testing

### **Test TTS:**

```python
from engine.command import speak

speak("Hello, this is a test of the ElevenLabs text to speech system.")
```

### **Test AI:**

```python
from engine.features import chatBot

response = chatBot("What is artificial intelligence?")
print(response)
```

### **Test Both:**

```bash
python run.py
# Say: "Hello, who are you?"
# Should get AI response with ElevenLabs voice
```

---

## 🐛 Troubleshooting

### **Issue: No sound from TTS**

**Check:**
1. Internet connection
2. API key is valid
3. Audio output device working
4. Check console for errors

**Solution:**
- System falls back to pyttsx3 automatically
- Check `www/assets/audio/` for temp files

### **Issue: AI not responding**

**Check:**
1. Internet connection
2. NVIDIA API key valid
3. Check console for error messages

**Solution:**
- System falls back to basic responses
- Check API key in `engine/config.py`

### **Issue: "Module not found: openai"**

**Solution:**
```bash
pip install openai
```

### **Issue: Rate limit exceeded**

**Solution:**
- Wait 60 seconds
- System automatically retries
- Falls back to basic responses

---

## 📊 Performance

### **Response Times:**

| Component | Time | Notes |
|-----------|------|-------|
| Speech Recognition | 2-3s | Google API |
| NVIDIA AI | 1-2s | Fast inference |
| ElevenLabs TTS | 1-2s | Audio generation |
| **Total** | **4-7s** | End-to-end |

### **Optimization:**

- ✅ Streaming disabled for consistency
- ✅ Max tokens limited to 200
- ✅ Temp files cleaned automatically
- ✅ Concurrent requests handled

---

## 🔄 Fallback System

### **TTS Fallback:**

```
ElevenLabs API
    ↓ (if fails)
pyttsx3 (local)
    ↓ (if fails)
Silent (log error)
```

### **AI Fallback:**

```
NVIDIA API
    ↓ (if fails)
Pattern Matching
    ↓ (if fails)
Generic Response
```

---

## 📈 Future Enhancements

### **Planned:**

- [ ] Voice selection UI
- [ ] Model selection UI
- [ ] Usage analytics dashboard
- [ ] Response caching
- [ ] Streaming responses
- [ ] Multi-language support
- [ ] Custom voice training

### **Under Consideration:**

- [ ] OpenAI GPT-4 integration
- [ ] Google Gemini support
- [ ] Anthropic Claude option
- [ ] Local LLM fallback (Ollama)

---

## 📚 API Documentation

### **ElevenLabs:**
- Docs: https://docs.elevenlabs.io/
- Dashboard: https://elevenlabs.io/app
- Full guide: `elevenlabs-api.md`

### **NVIDIA:**
- Docs: https://docs.api.nvidia.com/
- Dashboard: https://build.nvidia.com/
- Full guide: `API.md`

---

## ✅ Verification Checklist

Before reporting issues:

- [ ] Installed `openai` package
- [ ] Installed `requests` package
- [ ] Internet connection working
- [ ] API keys in `engine/config.py`
- [ ] Audio output device working
- [ ] Checked console for errors
- [ ] Tested with simple query

---

## 🎯 Quick Commands to Test

```
"Hello" → AI greeting + ElevenLabs voice
"What time is it?" → Current time
"Who are you?" → AI identity response
"Tell me a joke" → AI-generated joke
"Thank you" → Polite response
```

---

**Vishwakarma AI - Premium API Integration**

*High-Quality Voice • Advanced AI • Seamless Experience*

© 2025 Vishwakarma Industries. All rights reserved.
