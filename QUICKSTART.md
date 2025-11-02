# Vishwakarma AI - Quick Start Guide

**© 2025 Vishwakarma Industries**

---

## 🚀 Get Started in 5 Minutes

### Step 1: Install Python
Ensure you have Python 3.8 or higher installed:
```bash
python --version
```

### Step 2: Setup Environment
```bash
# Navigate to project directory
cd jarvis-main

# Create virtual environment
python -m venv envvishwakarma

# Activate virtual environment
# Windows:
envvishwakarma\Scripts\activate
# Linux/Mac:
source envvishwakarma/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Face Recognition (First Time Only)

#### Capture Your Face Samples
```bash
python engine/auth/sample.py
```
- Enter a numeric user ID (e.g., 1)
- Look at the camera
- 100 samples will be captured automatically

#### Train the Model
```bash
python engine/auth/trainer.py
```
Wait for "Model trained" message.

### Step 5: Launch Vishwakarma AI
```bash
python run.py
```

---

## 🎤 Voice Commands Examples

### Opening Applications
- "Open Chrome"
- "Open Notepad"
- "Open Calculator"

### YouTube
- "Play Imagine Dragons on YouTube"
- "Play coding tutorial on YouTube"

### Communication
- "Send message to John"
- "Call Mom"
- "Video call Sarah"

### General Queries
- "What's the weather?"
- "Tell me a joke"
- "What is artificial intelligence?"

---

## ⌨️ Keyboard Shortcuts

- **Win + J** - Activate voice input
- **ESC** - Exit face authentication
- **Enter** - Send text message in chat

---

## 🔧 Quick Configuration

### Add Applications to Database
```python
# Run Python shell
python

# Add system command
import sqlite3
con = sqlite3.connect("vishwakarma.db")
cursor = con.cursor()
cursor.execute("INSERT INTO sys_command VALUES (null,'chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')")
con.commit()
con.close()
```

### Add Websites
```python
cursor.execute("INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')")
con.commit()
```

### Add Contacts
```python
cursor.execute("INSERT INTO contacts VALUES (null,'John Doe', '9876543210', 'john@example.com')")
con.commit()
```

---

## 📱 Android Setup (Optional)

### Enable ADB on Android
1. Go to Settings → About Phone
2. Tap "Build Number" 7 times
3. Go to Settings → Developer Options
4. Enable "USB Debugging"
5. Connect phone via USB

### Run Device Setup
```bash
device.bat
```

---

## ❓ Troubleshooting

### Issue: Face Authentication Fails
**Solution:** Ensure good lighting and recapture face samples

### Issue: Microphone Not Working
**Solution:** Check microphone permissions in Windows settings

### Issue: Wake Word Not Detected
**Solution:** Speak clearly and ensure microphone is working

### Issue: Module Not Found Error
**Solution:** Ensure virtual environment is activated and dependencies installed

---

## 📞 Need Help?

Refer to the full [README.md](README.md) for detailed documentation.

---

**Vishwakarma AI** - Crafting Intelligence, Building Solutions

© 2025 Vishwakarma Industries. All rights reserved.
