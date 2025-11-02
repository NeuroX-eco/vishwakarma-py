# Vishwakarma AI - Troubleshooting Guide

**© 2025 Vishwakarma Industries**

---

## 🔧 Common Issues & Solutions

### **1. Speech Recognition Errors**

#### Issue: "Could not understand audio"
**Cause:** Background noise, unclear speech, or microphone issues

**Solutions:**
- Speak clearly and at normal pace
- Reduce background noise
- Check microphone is working
- Adjust microphone volume in Windows settings
- Move closer to microphone

#### Issue: "Could not request results"
**Cause:** No internet connection

**Solutions:**
- Check internet connection
- Verify Google Speech API is accessible
- Try restarting your router
- Check firewall settings

---

### **2. Chatbot Errors**

#### Issue: "Cookies file not found"
**Cause:** Missing `engine/cookies.json` file

**Solutions:**
1. Create HuggingChat account
2. Export cookies from browser
3. Save as `engine/cookies.json`
4. Ensure file path is correct

#### Issue: "Chatbot connection failed"
**Cause:** Invalid cookies or network issues

**Solutions:**
- Refresh cookies from HuggingChat
- Check internet connection
- Verify cookies.json format is valid JSON

---

### **3. Face Recognition Issues**

#### Issue: "No trained model found"
**Cause:** Model not trained yet

**Solutions:**
```bash
# Capture samples first
python engine/auth/sample.py

# Then train model
python engine/auth/trainer.py
```

#### Issue: "Face not recognized"
**Cause:** Poor lighting or model not trained properly

**Solutions:**
- Improve lighting conditions
- Recapture face samples
- Retrain the model
- Ensure camera is working

---

### **4. Application/Website Opening Errors**

#### Issue: "Application not found"
**Cause:** App not in database or incorrect path

**Solutions:**
1. Add to database:
```sql
INSERT INTO sys_command (name, path) 
VALUES ('appname', 'C:\\Path\\To\\App.exe');
```

2. Or add website:
```sql
INSERT INTO web_command (name, url) 
VALUES ('google', 'https://www.google.com');
```

---

### **5. WhatsApp/Call Features**

#### Issue: "Contact not found"
**Cause:** Contact not in database

**Solutions:**
1. Add contact to `contacts.csv`:
```csv
Name,Mobile
John Doe,9876543210
```

2. Import to database or add manually

#### Issue: "ADB not found"
**Cause:** Android Debug Bridge not installed

**Solutions:**
- Install ADB tools
- Add ADB to system PATH
- Enable USB debugging on phone
- Connect phone via USB

---

### **6. Audio/Sound Issues**

#### Issue: "No sound from assistant"
**Cause:** Audio output issues or TTS engine problem

**Solutions:**
- Check system volume
- Verify speakers/headphones connected
- Test TTS engine:
```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Test")
engine.runAndWait()
```

#### Issue: "Microphone not working"
**Cause:** Microphone permissions or hardware issue

**Solutions:**
- Check Windows microphone permissions
- Test microphone in other apps
- Select correct input device
- Update audio drivers

---

### **7. Database Errors**

#### Issue: "Database locked"
**Cause:** Multiple processes accessing database

**Solutions:**
- Close other instances of Vishwakarma AI
- Restart the application
- Check for zombie processes

#### Issue: "Table not found"
**Cause:** Database not initialized

**Solutions:**
- Ensure `vishwakarma.db` exists
- Run database initialization if needed
- Check database file permissions

---

### **8. Import/Module Errors**

#### Issue: "Module not found: cv2"
**Solutions:**
```bash
pip install opencv-python opencv-contrib-python
```

#### Issue: "Module not found: pyttsx3"
**Solutions:**
```bash
pip install pyttsx3
```

#### Issue: "Module not found: speech_recognition"
**Solutions:**
```bash
pip install SpeechRecognition
```

---

### **9. UI/Display Issues**

#### Issue: "Blank screen or UI not loading"
**Cause:** Browser/Eel issues

**Solutions:**
- Clear browser cache
- Try different browser
- Check if port 8000 is available
- Restart the application

#### Issue: "Animations not working"
**Cause:** JavaScript errors or network issues

**Solutions:**
- Check browser console for errors
- Verify internet connection (for CDN resources)
- Refresh the page

---

### **10. Performance Issues**

#### Issue: "Slow response time"
**Cause:** System resources or network latency

**Solutions:**
- Close unnecessary applications
- Check internet speed
- Reduce animation complexity
- Upgrade system RAM if needed

#### Issue: "High CPU usage"
**Cause:** Continuous speech recognition

**Solutions:**
- Use push-to-talk (Win+J)
- Reduce recognition timeout
- Close background applications

---

## 🐛 Error Messages Explained

### "Error processing command"
- **Meaning:** General command processing failure
- **Check:** Console for specific error details
- **Action:** Review command syntax and try again

### "Something went wrong"
- **Meaning:** Unexpected error in feature execution
- **Check:** Logs for stack trace
- **Action:** Report issue with error details

### "Empty query received"
- **Meaning:** No speech detected or recognized
- **Check:** Microphone is working
- **Action:** Speak louder or closer to mic

---

## 📊 Diagnostic Commands

### Check Python Environment
```bash
python --version
pip list
```

### Check Microphone
```python
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print(r.recognize_google(audio))
```

### Check TTS
```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Testing text to speech")
engine.runAndWait()
```

### Check Camera
```python
import cv2
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
print(f"Camera working: {ret}")
cam.release()
```

---

## 🔍 Debugging Tips

### Enable Verbose Logging
Add to your code:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Console Output
- Run from terminal to see all print statements
- Look for stack traces
- Note error messages

### Test Components Individually
- Test speech recognition alone
- Test TTS alone
- Test face recognition alone
- Test database queries alone

---

## 📝 Log Files

### Where to Find Logs
- Console output (terminal)
- Windows Event Viewer
- Application-specific logs (if configured)

### What to Log
- Error messages
- Stack traces
- User commands
- System responses
- Timestamps

---

## 🆘 Getting Help

### Before Reporting Issues
1. Check this troubleshooting guide
2. Review error messages
3. Test with minimal configuration
4. Document steps to reproduce

### Information to Provide
- Error message (exact text)
- Steps to reproduce
- System information (OS, Python version)
- Relevant log output
- Configuration details

---

## 🔄 Reset/Reinstall

### Soft Reset
```bash
# Deactivate and reactivate environment
deactivate
envvishwakarma\Scripts\activate

# Restart application
python run.py
```

### Hard Reset
```bash
# Backup database
copy vishwakarma.db vishwakarma_backup.db

# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Restart
python run.py
```

### Complete Reinstall
```bash
# Remove virtual environment
rmdir /s envvishwakarma

# Create fresh environment
python -m venv envvishwakarma
envvishwakarma\Scripts\activate
pip install -r requirements.txt

# Restart
python run.py
```

---

## ✅ Prevention Tips

### Regular Maintenance
- Update dependencies monthly
- Clear cache periodically
- Backup database regularly
- Test after updates

### Best Practices
- Use stable internet connection
- Keep system updated
- Monitor resource usage
- Document custom changes

---

**Vishwakarma AI - Reliable Performance**

*Crafting Intelligence, Building Solutions*

© 2025 Vishwakarma Industries. All rights reserved.
