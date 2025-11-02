# 🔑 API Configuration Guide

## NVIDIA API Setup

This voice assistant uses **NVIDIA's AI Foundation Models** through their API service.

### Current API Key

```
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
```

⚠️ **Security Note**: This API key is currently hardcoded in the script. For production use, follow the security best practices below.

---

## How to Get Your Own API Key

### Step 1: Sign Up for NVIDIA AI

1. Visit [NVIDIA AI Foundation Models](https://build.nvidia.com/)
2. Click **"Sign In"** or **"Get Started"**
3. Create an account or sign in with existing NVIDIA account
4. Accept the terms and conditions

### Step 2: Generate API Key

1. Navigate to your **Dashboard** or **API Keys** section
2. Click **"Generate API Key"** or **"Create New Key"**
3. Copy the generated API key (starts with `nvapi-`)
4. Store it securely

### Step 3: Configure the Voice Assistant

Replace the API key in `voice_assistant.py`:

```python
# Initialize OpenAI client with NVIDIA API
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY_HERE"  # Replace with your key
)
```

---

## API Configuration Methods

### Method 1: Environment Variable (Recommended)

**Windows PowerShell:**
```powershell
$env:NVIDIA_API_KEY = "your-api-key-here"
python voice_assistant.py
```

**Windows Command Prompt:**
```cmd
set NVIDIA_API_KEY=your-api-key-here
python voice_assistant.py
```

**Permanent (Windows):**
1. Open System Properties → Advanced → Environment Variables
2. Add new User Variable:
   - Name: `NVIDIA_API_KEY`
   - Value: `your-api-key-here`

**Update code to use environment variable:**
```python
import os

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
```

### Method 2: .env File (Recommended)

1. **Install python-dotenv:**
```bash
pip install python-dotenv
```

2. **Create `.env` file** in project directory:
```env
NVIDIA_API_KEY=your-api-key-here
```

3. **Update code:**
```python
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
```

4. **Add `.env` to `.gitignore`:**
```
.env
```

### Method 3: Config File

1. **Create `config.json`:**
```json
{
    "nvidia_api_key": "your-api-key-here",
    "model": "openai/gpt-oss-120b",
    "temperature": 0.7,
    "max_tokens": 500
}
```

2. **Update code:**
```python
import json

with open('config.json', 'r') as f:
    config = json.load(f)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=config['nvidia_api_key']
)
```

3. **Add `config.json` to `.gitignore`**

---

## Available Models

### Current Model: `openai/gpt-oss-120b`

Other available models on NVIDIA API:

| Model | Description | Best For |
|-------|-------------|----------|
| `openai/gpt-oss-120b` | Large language model | General conversation |
| `meta/llama-3.1-405b-instruct` | Meta's Llama 3.1 | Advanced reasoning |
| `mistralai/mixtral-8x7b-instruct` | Mixtral model | Fast responses |
| `google/gemma-7b` | Google's Gemma | Efficient processing |

### Change Model

```python
completion = client.chat.completions.create(
    model="meta/llama-3.1-405b-instruct",  # Change model here
    messages=messages_to_send,
    temperature=0.7,
    top_p=0.9,
    max_tokens=500,
    stream=True
)
```

---

## API Parameters

### Temperature
Controls randomness in responses.

```python
temperature=0.7  # Range: 0.0 - 1.0
```

- **0.0-0.3**: More focused and deterministic
- **0.4-0.7**: Balanced (recommended for voice assistant)
- **0.8-1.0**: More creative and random

### Top P
Controls diversity via nucleus sampling.

```python
top_p=0.9  # Range: 0.0 - 1.0
```

- **0.9**: Recommended default
- Lower values: More focused responses
- Higher values: More diverse responses

### Max Tokens
Maximum length of response.

```python
max_tokens=500  # Adjust based on needs
```

- **100-300**: Short, concise answers
- **500**: Balanced (current setting)
- **1000+**: Longer, detailed responses

### Streaming
Enable real-time response streaming.

```python
stream=True  # True for real-time, False for complete response
```

---

## API Usage Limits

### Free Tier
- Limited requests per minute
- May have rate limiting
- Suitable for development and testing

### Rate Limiting
If you encounter rate limits:

```python
import time

try:
    completion = client.chat.completions.create(...)
except Exception as e:
    if "rate limit" in str(e).lower():
        print("Rate limit reached. Waiting...")
        time.sleep(5)
        # Retry request
```

---

## Error Handling

### Common Errors

**1. Invalid API Key**
```
Error: 401 Unauthorized
```
**Solution**: Check your API key is correct

**2. Rate Limit Exceeded**
```
Error: 429 Too Many Requests
```
**Solution**: Wait and retry, or upgrade plan

**3. Network Error**
```
Error: Connection timeout
```
**Solution**: Check internet connection

### Implement Error Handling

```python
def get_ai_response(user_input):
    try:
        completion = client.chat.completions.create(...)
        # Process response
    except Exception as e:
        if "401" in str(e):
            return "API key is invalid. Please check your configuration."
        elif "429" in str(e):
            return "Rate limit exceeded. Please try again in a moment."
        elif "timeout" in str(e).lower():
            return "Network timeout. Please check your connection."
        else:
            return f"Error: {str(e)}"
```

---

## Testing Your API Key

### Quick Test Script

Create `test_api.py`:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY_HERE"
)

try:
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": "Hello, are you working?"}],
        max_tokens=50
    )
    
    response = completion.choices[0].message.content
    print(f"✅ API is working! Response: {response}")
    
except Exception as e:
    print(f"❌ API Error: {e}")
```

Run:
```bash
python test_api.py
```

---

## Security Best Practices

### ✅ DO:
- Store API keys in environment variables
- Use `.env` files for local development
- Add `.env` and `config.json` to `.gitignore`
- Rotate API keys regularly
- Use different keys for development and production
- Monitor API usage

### ❌ DON'T:
- Hardcode API keys in source code
- Commit API keys to version control (Git)
- Share API keys publicly
- Use production keys in development
- Expose keys in client-side code

---

## Alternative APIs

If you want to use different AI providers:

### OpenAI GPT-4
```python
from openai import OpenAI

client = OpenAI(
    api_key="your-openai-api-key"
)

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Anthropic Claude
```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-anthropic-api-key"
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Google Gemini
```python
import google.generativeai as genai

genai.configure(api_key="your-google-api-key")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello")
```

---

## Monitoring API Usage

### Log API Calls

```python
import logging

logging.basicConfig(filename='api_usage.log', level=logging.INFO)

def get_ai_response(user_input):
    logging.info(f"API Request: {user_input}")
    
    try:
        completion = client.chat.completions.create(...)
        logging.info(f"API Response: Success")
        return response_text
    except Exception as e:
        logging.error(f"API Error: {e}")
        return error_message
```

### Track Costs

Keep track of:
- Number of requests
- Tokens used per request
- Total tokens per day/month
- Estimated costs

---

## Troubleshooting

### Issue: "Module 'openai' not found"
**Solution:**
```bash
pip install openai
```

### Issue: "Connection refused"
**Solution:**
- Check internet connection
- Verify API endpoint URL
- Check firewall settings

### Issue: "Invalid model"
**Solution:**
- Verify model name is correct
- Check available models in NVIDIA catalog
- Ensure model is accessible with your API tier

---

## Support and Resources

### Official Documentation
- [NVIDIA AI Foundation Models](https://build.nvidia.com/)
- [API Documentation](https://docs.api.nvidia.com/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

### Community
- [NVIDIA Developer Forums](https://forums.developer.nvidia.com/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/nvidia)

### Contact
For API issues:
- Email: support@nvidia.com
- Developer Portal: https://developer.nvidia.com/

---

## Quick Reference

### Essential Code Snippet

```python
from openai import OpenAI
import os

# Load API key from environment
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY", "fallback-key-here")
)

# Make API call
def chat(message):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
            max_tokens=500,
            stream=True
        )
        
        result = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                result += chunk.choices[0].delta.content
        
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## Updates and Changelog

### Version 1.0 (Current)
- Initial API integration
- NVIDIA GPT-OSS-120B model
- Streaming responses
- Basic error handling

### Future Enhancements
- Multi-model support
- Advanced error recovery
- Usage analytics
- Cost optimization
- Caching frequently asked questions

---

**Last Updated**: October 31, 2025  
**API Version**: v1  
**SDK Version**: openai>=1.0.0
