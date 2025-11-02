# 🎙️ ElevenLabs Text-to-Speech API Guide

## 🔑 API Key Configuration

**Your API Key:**
```
sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58
```

### Available Voices

#### Male Voices

**1. Viraj (Default)**
- **Voice ID:** `iWNf11sz1GrUE4ppxTOL`
- **Voice Link:** https://elevenlabs.io/app/voice-library?voiceId=iWNf11sz1GrUE4ppxTOL
- **Description:** Helpful Customer Care Agent
- **Language:** Hindi (hi-IN)
- **Use Case:** Customer service, support bots

**2. Male Voice**
- **Voice ID:** `u7bRcYbD7visSINTyAT8`
- **Voice Link:** https://elevenlabs.io/app/voice-library?voiceId=u7bRcYbD7visSINTyAT8

#### Female Voices

**1. Female Voice 1**
- **Voice ID:** `NHRgOEwqx5WZNClv5sat`
- **Voice Link:** https://elevenlabs.io/app/voice-library?voiceId=NHRgOEwqx5WZNClv5sat

**2. Female Voice 2**
- **Voice ID:** `jUjRbhZWoMK4aDciW36V`
- **Voice Link:** https://elevenlabs.io/app/voice-library?voiceId=jUjRbhZWoMK4aDciW36V

---

---

## 📋 Quick Start

### Installation

```bash
# Install required packages
pip install requests

# Or use official ElevenLabs SDK (recommended)
pip install elevenlabs
```

---

## 🚀 Usage Examples

### Method 1: Using Official ElevenLabs SDK (Recommended)

```python
from elevenlabs import generate, play, save, set_api_key, voices

# Set your API key
set_api_key("sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58")

# Generate speech with Viraj voice (Male - Hindi)
audio = generate(
    text="Hello! This is a test using the Viraj voice.",
    voice="iWNf11sz1GrUE4ppxTOL",
    model="eleven_monolingual_v1"
)

# Save to file
save(audio, "output.mp3")

# Or play directly
play(audio)
```

### Using Different Voices

```python
from elevenlabs import generate, save, set_api_key

set_api_key("sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58")

# Voice IDs
VOICES = {
    "viraj_male": "iWNf11sz1GrUE4ppxTOL",      # Male - Hindi
    "male_voice": "u7bRcYbD7visSINTyAT8",      # Male
    "female_voice_1": "NHRgOEwqx5WZNClv5sat",  # Female
    "female_voice_2": "jUjRbhZWoMK4aDciW36V"   # Female
}

# Generate with male voice
audio_male = generate(
    text="This is a male voice example.",
    voice=VOICES["male_voice"],
    model="eleven_multilingual_v2"
)
save(audio_male, "male_output.mp3")

# Generate with female voice 1
audio_female1 = generate(
    text="This is a female voice example.",
    voice=VOICES["female_voice_1"],
    model="eleven_multilingual_v2"
)
save(audio_female1, "female1_output.mp3")

# Generate with female voice 2
audio_female2 = generate(
    text="This is another female voice example.",
    voice=VOICES["female_voice_2"],
    model="eleven_multilingual_v2"
)
save(audio_female2, "female2_output.mp3")

print("✅ All voices generated successfully!")
```

### Method 2: Using Requests Library (REST API)

```python
import requests

API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"
BASE_URL = "https://api.elevenlabs.io/v1"

# Voice IDs
VOICES = {
    "viraj_male": "iWNf11sz1GrUE4ppxTOL",      # Male - Hindi
    "male_voice": "u7bRcYbD7visSINTyAT8",      # Male
    "female_voice_1": "NHRgOEwqx5WZNClv5sat",  # Female
    "female_voice_2": "jUjRbhZWoMK4aDciW36V"   # Female
}

def text_to_speech(text, voice_id, output_file="output.mp3"):
    """Convert text to speech using ElevenLabs API"""
    
    url = f"{BASE_URL}/text-to-speech/{voice_id}"
    
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.61,
            "similarity_boost": 0.24,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"✅ Audio saved to {output_file}")
        return True
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return False

# Example usage with different voices
text_to_speech("Hello, this is Viraj speaking!", VOICES["viraj_male"], "viraj_output.mp3")
text_to_speech("This is a male voice.", VOICES["male_voice"], "male_output.mp3")
text_to_speech("This is a female voice.", VOICES["female_voice_1"], "female1_output.mp3")
text_to_speech("Another female voice example.", VOICES["female_voice_2"], "female2_output.mp3")
```

---

## 🎤 Voice Information: Viraj

**Name:** Viraj - Helpful Customer Care Agent  
**Voice ID:** `iWNf11sz1GrUE4ppxTOL`  
**Category:** Professional  
**Language:** Hindi (hi-IN)  
**Gender:** Male  
**Age:** Young  
**Accent:** Standard  

**Description:**
A friendly, upbeat voice designed to make every customer feel heard and reassured. Viraj's tone blends energy with empathy—ideal for dynamic support bots, voice-based helpdesk systems, and human-like AI calling.

**Best Use Cases:**
- Customer care hotlines
- AI calling apps
- WhatsApp voice assistants
- Telecom services
- Fintech applications
- Retail customer service
- Support bots

**Default Settings:**
- Stability: 0.61
- Similarity Boost: 0.24

---

## 🎛️ Voice Settings Guide

### Stability (0.0 - 1.0)

Controls the consistency of the voice output.

```python
voice_settings = {
    "stability": 0.5  # Adjust between 0.0 and 1.0
}
```

- **0.0 - 0.3:** More expressive, variable, emotional
- **0.4 - 0.7:** Balanced (recommended for most use cases)
- **0.8 - 1.0:** Very consistent, stable, monotone

**Recommendation:** Use 0.5-0.7 for conversational AI, 0.3-0.5 for storytelling

### Similarity Boost (0.0 - 1.0)

Controls how closely the output matches the original voice.

```python
voice_settings = {
    "similarity_boost": 0.75  # Adjust between 0.0 and 1.0
}
```

- **0.0 - 0.4:** More creative interpretation
- **0.5 - 0.7:** Balanced
- **0.8 - 1.0:** Very close to original voice

**Recommendation:** Use 0.7-0.8 for professional applications

### Style (0.0 - 1.0)

Controls the style exaggeration (available in some models).

```python
voice_settings = {
    "style": 0.0  # Adjust between 0.0 and 1.0
}
```

- **0.0:** Neutral
- **0.5:** Moderate style
- **1.0:** Maximum style exaggeration

### Speaker Boost

Enhances voice clarity and quality.

```python
voice_settings = {
    "use_speaker_boost": True  # True or False
}
```

**Recommendation:** Keep `True` for best quality

---

## 🔧 Advanced Usage Examples

### Example 1: Batch Text-to-Speech

```python
from elevenlabs import generate, save, set_api_key

set_api_key("sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58")

texts = [
    "Welcome to our customer service.",
    "How can I help you today?",
    "Thank you for calling. Have a great day!"
]

for i, text in enumerate(texts, 1):
    audio = generate(
        text=text,
        voice="iWNf11sz1GrUE4ppxTOL",
        model="eleven_monolingual_v1"
    )
    save(audio, f"audio_{i}.mp3")
    print(f"Generated audio_{i}.mp3")
```

### Example 2: Custom Voice Settings

```python
import requests

API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"
VOICE_ID = "iWNf11sz1GrUE4ppxTOL"

def text_to_speech_custom(text, stability=0.5, similarity=0.75):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Generate with custom settings
audio = text_to_speech_custom(
    "Hello, this is a custom voice test!",
    stability=0.7,
    similarity=0.8
)

with open("custom_output.mp3", "wb") as f:
    f.write(audio)
```

### Example 3: Stream Audio (Real-time)

```python
import requests

API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"
VOICE_ID = "iWNf11sz1GrUE4ppxTOL"

def stream_text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.61,
            "similarity_boost": 0.24
        }
    }
    
    response = requests.post(url, headers=headers, json=payload, stream=True)
    
    if response.status_code == 200:
        with open("streamed_output.mp3", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("✅ Streaming complete!")
    else:
        print(f"❌ Error: {response.status_code}")

# Use streaming for faster response
stream_text_to_speech("This is a streaming test!")
```

### Example 4: Get Available Voices

```python
import requests

API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"

def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        voices = response.json()['voices']
        for voice in voices:
            print(f"Name: {voice['name']}")
            print(f"ID: {voice['voice_id']}")
            print(f"Category: {voice.get('category', 'N/A')}")
            print("-" * 50)
    else:
        print(f"Error: {response.status_code}")

get_voices()
```

### Example 5: Check Usage/Quota

```python
import requests

API_KEY = "sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58"

def check_usage():
    url = "https://api.elevenlabs.io/v1/user"
    headers = {"xi-api-key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        subscription = user_data.get('subscription', {})
        
        char_count = subscription.get('character_count', 0)
        char_limit = subscription.get('character_limit', 0)
        
        print(f"Characters Used: {char_count:,}")
        print(f"Character Limit: {char_limit:,}")
        
        if char_limit > 0:
            usage_percent = (char_count / char_limit) * 100
            print(f"Usage: {usage_percent:.1f}%")
            print(f"Remaining: {char_limit - char_count:,} characters")
    else:
        print(f"Error: {response.status_code}")

check_usage()
```

---

## 🌐 Available Models

| Model ID | Description | Best For | Languages |
|----------|-------------|----------|-----------|
| `eleven_monolingual_v1` | English only, fast | English content | English |
| `eleven_multilingual_v1` | Multiple languages | International content | 29+ languages |
| `eleven_multilingual_v2` | Latest multilingual | Best quality | 29+ languages |
| `eleven_turbo_v2` | Fastest, low latency | Real-time apps | English + others |

**Recommendation:** Use `eleven_multilingual_v2` for best quality with Hindi content.

---

## 📊 API Endpoints Reference

### Base URL
```
https://api.elevenlabs.io/v1
```

### Authentication
All requests require the API key in the header:
```
xi-api-key: sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58
```

### Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/text-to-speech/{voice_id}` | POST | Generate speech |
| `/text-to-speech/{voice_id}/stream` | POST | Stream speech (real-time) |
| `/voices` | GET | List all voices |
| `/voices/{voice_id}` | GET | Get voice details |
| `/user` | GET | Get user info & quota |
| `/history` | GET | Get generation history |

---

## 💡 Best Practices

### 1. Text Optimization

```python
# ✅ Good: Clear, well-punctuated text
text = "Hello! How can I help you today? Please let me know."

# ❌ Avoid: Long sentences without punctuation
text = "Hello how can I help you today please let me know if you need anything"
```

### 2. Error Handling

```python
import requests

def safe_text_to_speech(text):
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.content
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None
```

### 3. Rate Limiting

```python
import time

def generate_multiple_with_delay(texts, delay=1):
    """Generate multiple audio files with delay between requests"""
    for i, text in enumerate(texts):
        audio = generate(text=text, voice="iWNf11sz1GrUE4ppxTOL")
        save(audio, f"output_{i}.mp3")
        time.sleep(delay)  # Avoid rate limiting
```

### 4. Caching

```python
import hashlib
import os

def cached_text_to_speech(text, cache_dir="audio_cache"):
    """Cache generated audio to avoid regenerating same text"""
    os.makedirs(cache_dir, exist_ok=True)
    
    # Create hash of text for filename
    text_hash = hashlib.md5(text.encode()).hexdigest()
    cache_file = f"{cache_dir}/{text_hash}.mp3"
    
    # Check if cached
    if os.path.exists(cache_file):
        print(f"Using cached audio for: {text[:50]}...")
        with open(cache_file, 'rb') as f:
            return f.read()
    
    # Generate new audio
    audio = generate(text=text, voice="iWNf11sz1GrUE4ppxTOL")
    
    # Save to cache
    with open(cache_file, 'wb') as f:
        f.write(audio)
    
    return audio
```

---

## 🔐 Security Best Practices

### 1. Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ELEVENLABS_API_KEY')
VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID')
```

Create `.env` file:
```
ELEVENLABS_API_KEY=sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58
ELEVENLABS_VOICE_ID=iWNf11sz1GrUE4ppxTOL
```

### 2. .gitignore

Add to `.gitignore`:
```
.env
elvenlabs-api.json
*.mp3
audio_cache/
```

### 3. API Key Rotation

- Rotate keys every 90 days
- Generate new keys from [ElevenLabs Dashboard](https://elevenlabs.io/app/settings/api-keys)
- Delete old keys after rotation

---

## 💰 Pricing & Limits

### Free Tier
- **10,000 characters/month**
- Access to all voices
- Standard quality

### Starter ($5/month)
- **30,000 characters/month**
- Commercial license
- Priority support

### Creator ($22/month)
- **100,000 characters/month**
- Voice cloning
- Advanced features

### Pro ($99/month)
- **500,000 characters/month**
- Professional features
- API access

### Scale ($330/month)
- **2,000,000 characters/month**
- Enterprise features
- Dedicated support

**Note:** Check [ElevenLabs Pricing](https://elevenlabs.io/pricing) for current rates.

---

## 🆘 Troubleshooting

### Error: 401 Unauthorized
**Cause:** Invalid API key  
**Solution:** Verify API key is correct and active

### Error: 404 Voice Not Found
**Cause:** Voice ID doesn't exist or not accessible  
**Solution:** Check voice ID or add voice to your library

### Error: 422 Unprocessable Entity
**Cause:** Invalid request parameters  
**Solution:** Check text length, voice settings, model ID

### Error: 429 Too Many Requests
**Cause:** Rate limit exceeded  
**Solution:** Implement delays between requests

### Error: 500 Internal Server Error
**Cause:** Server-side issue  
**Solution:** Retry after a few seconds

### Poor Audio Quality
**Solutions:**
- Increase `similarity_boost` (0.7-0.9)
- Adjust `stability` (0.5-0.7)
- Enable `use_speaker_boost`
- Use `eleven_multilingual_v2` model

---

## 📚 Additional Resources

- **Official Documentation:** https://docs.elevenlabs.io/
- **API Reference:** https://elevenlabs.io/docs/api-reference
- **Voice Library:** https://elevenlabs.io/voice-library
- **Dashboard:** https://elevenlabs.io/app
- **Python SDK:** https://github.com/elevenlabs/elevenlabs-python
- **Support:** support@elevenlabs.io

---

## 📝 Quick Reference Card

```python
# Import
from elevenlabs import generate, save, set_api_key

# Setup
set_api_key("sk_3ffdb4616e99bfab452607e6efe5c7de6941ada4c5717a58")

# Generate
audio = generate(
    text="Your text here",
    voice="iWNf11sz1GrUE4ppxTOL",
    model="eleven_multilingual_v2"
)

# Save
save(audio, "output.mp3")
```

---

## 🎯 Voice ID Quick Reference

| Voice Name | Gender | Voice ID | Voice Link |
|------------|--------|----------|------------|
| **Viraj** (Hindi) | Male | `iWNf11sz1GrUE4ppxTOL` | [Open](https://elevenlabs.io/app/voice-library?voiceId=iWNf11sz1GrUE4ppxTOL) |
| **Male Voice** | Male | `u7bRcYbD7visSINTyAT8` | [Open](https://elevenlabs.io/app/voice-library?voiceId=u7bRcYbD7visSINTyAT8) |
| **Female Voice 1** | Female | `NHRgOEwqx5WZNClv5sat` | [Open](https://elevenlabs.io/app/voice-library?voiceId=NHRgOEwqx5WZNClv5sat) |
| **Female Voice 2** | Female | `jUjRbhZWoMK4aDciW36V` | [Open](https://elevenlabs.io/app/voice-library?voiceId=jUjRbhZWoMK4aDciW36V) |

### Copy-Paste Voice Dictionary

```python
VOICES = {
    "viraj_male": "iWNf11sz1GrUE4ppxTOL",      # Male - Hindi - Customer Care
    "male_voice": "u7bRcYbD7visSINTyAT8",      # Male
    "female_voice_1": "NHRgOEwqx5WZNClv5sat",  # Female
    "female_voice_2": "jUjRbhZWoMK4aDciW36V"   # Female
}
```

---

**Last Updated:** 2025-11-01  
**API Version:** v1  
**Total Voices:** 4 (2 Male, 2 Female)
