# ⚡ Quick Start Guide - Vishwakarma AI

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure API Keys
```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your API keys
notepad .env
```

**Add these keys to `.env`**:
```env
ELEVENLABS_API_KEY=your_elevenlabs_key_here
NVIDIA_API_KEY=your_nvidia_key_here
```

### Step 3: Run the Application
```bash
python run.py
```

---

## 🔑 Get Your API Keys

### ElevenLabs (Text-to-Speech)
1. Visit: https://elevenlabs.io/
2. Sign up (free)
3. Go to Profile → API Keys
4. Copy your key (starts with `sk_`)

### NVIDIA AI (Chatbot)
1. Visit: https://build.nvidia.com/
2. Sign up (free)
3. Go to API Keys section
4. Copy your key (starts with `nvapi-`)

---

## ⚠️ Important Notes

- **Don't have API keys?** The app will still work with fallback methods!
- **Free tiers available** for both APIs
- **Secure by default** - API keys are never committed to Git
- **Need help?** Check `API_SETUP.md` for detailed instructions

---

## 🎯 What Works Without API Keys

### Without ElevenLabs:
- ✅ Uses Windows built-in TTS (pyttsx3)
- ✅ All features work, just different voice

### Without NVIDIA AI:
- ✅ Uses pattern-matching chatbot
- ✅ Handles basic queries (greetings, time, date)

---

## 🆘 Troubleshooting

### "Module not found: dotenv"
```bash
pip install python-dotenv
```

### "API key not set" warning
- Create `.env` file from `.env.example`
- Add your actual API keys
- Restart the application

### Application won't start
1. Check Python version (3.8+)
2. Install all dependencies
3. Check console for error messages

---

## 📚 More Information

- **Detailed Setup**: See `API_SETUP.md`
- **All Fixes**: See `API_FIXES_SUMMARY.md`
- **Troubleshooting**: See `TROUBLESHOOTING.md`
- **Full Documentation**: See `README.md`

---

**Ready to go? Run `python run.py` and enjoy Vishwakarma AI! 🎉**
