# Vishwakarma AI - Face Recognition Setup Guide

**© 2025 Vishwakarma Industries**

---

## 🎭 Face Recognition System

Vishwakarma AI uses advanced LBPH (Local Binary Patterns Histograms) face recognition for secure authentication.

---

## 📋 Prerequisites

- **Webcam** - Built-in or external camera
- **Good lighting** - Natural or artificial light
- **Clear view** - Face the camera directly
- **Python environment** - Activated virtual environment

---

## 🚀 Setup Process

### **Step 1: Capture Face Samples**

Run the sample capture script:

```bash
python engine/auth/sample.py
```

**What happens:**
- Camera window opens
- Enter a numeric **User ID** (e.g., 1, 2, 3...)
- Press Enter
- **100 face samples** will be captured automatically
- Look at the camera from different angles
- Samples saved in `engine/auth/samples/`

**Tips for best results:**
- ✅ Face the camera directly
- ✅ Move your head slightly (left, right, up, down)
- ✅ Maintain good lighting
- ✅ Remove glasses temporarily
- ✅ Keep a neutral expression
- ✅ Stay within camera frame

### **Step 2: Train the Model**

After capturing samples, train the recognition model:

```bash
python engine/auth/trainer.py
```

**What happens:**
- Reads all face samples
- Trains LBPH face recognizer
- Creates `trainer.yml` model file
- Saves in `engine/auth/trainer/`

**Output:**
```
Training faces. It will take a few seconds. Wait...
Model trained
```

### **Step 3: Test Authentication**

Launch Vishwakarma AI:

```bash
python run.py
```

The system will:
1. Show face authentication screen
2. Scan your face
3. Match against trained model
4. Grant access if recognized

---

## 👥 Multiple Users

### Adding Additional Users

1. **Capture samples for each user:**
   ```bash
   python engine/auth/sample.py
   ```
   - User 1: ID = 1
   - User 2: ID = 2
   - User 3: ID = 3
   - etc.

2. **Retrain the model:**
   ```bash
   python engine/auth/trainer.py
   ```
   - Model will include all users

3. **Update names in code:**
   Edit `engine/auth/recoganize.py`:
   ```python
   names = ['', 'User1', 'User2', 'User3']
   ```

---

## 🔧 Troubleshooting

### Camera Not Working

**Issue:** Camera doesn't open

**Solutions:**
- Check camera permissions in Windows settings
- Ensure no other app is using the camera
- Try different camera index:
  ```python
  cam = cv2.VideoCapture(1)  # Try 1, 2, etc.
  ```

### Face Not Detected

**Issue:** "Face not detected" message

**Solutions:**
- Improve lighting conditions
- Move closer to camera
- Ensure face is clearly visible
- Check if Haar Cascade file exists:
  ```
  engine/auth/haarcascade_frontalface_default.xml
  ```

### Authentication Fails

**Issue:** Face recognized as "unknown"

**Solutions:**
- Recapture face samples with better lighting
- Capture more samples (increase count in sample.py)
- Retrain the model
- Adjust recognition threshold in code

### Low Accuracy

**Issue:** Recognition accuracy < 50%

**Solutions:**
- Capture samples in similar lighting as authentication
- Capture more varied angles
- Ensure consistent distance from camera
- Clean camera lens

---

## 📁 File Structure

```
engine/auth/
├── haarcascade_frontalface_default.xml  # Face detection model
├── sample.py                             # Capture face samples
├── trainer.py                            # Train recognition model
├── recoganize.py                         # Authentication logic
├── samples/                              # Captured face images
│   ├── User.1.1.jpg
│   ├── User.1.2.jpg
│   └── ...
└── trainer/
    └── trainer.yml                       # Trained model
```

---

## ⚙️ Configuration

### Adjust Sample Count

Edit `engine/auth/sample.py`:

```python
count = 0
while True:
    ret, img = cam.read()
    # ...
    count += 1
    if count >= 100:  # Change this number
        break
```

### Adjust Recognition Threshold

Edit `engine/auth/recoganize.py`:

```python
if (accuracy < 100):  # Lower = stricter, Higher = lenient
    # Face recognized
```

### Change Camera Resolution

Edit `engine/auth/sample.py` or `recoganize.py`:

```python
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height
```

---

## 🎯 Best Practices

### For Capturing Samples

1. **Consistent Environment**
   - Capture in same lighting as you'll use the system
   - Same background if possible

2. **Varied Angles**
   - Straight on (most samples)
   - Slight left/right turns
   - Slight up/down tilts

3. **Natural Expression**
   - Neutral face (most samples)
   - Slight smile (some samples)
   - Avoid extreme expressions

4. **Accessories**
   - Capture with and without glasses
   - Different hairstyles if applicable

### For Authentication

1. **Optimal Conditions**
   - Good, even lighting
   - Face camera directly
   - Stay still during scan
   - Remove obstructions

2. **Consistent Setup**
   - Same camera position
   - Similar distance
   - Similar lighting

---

## 🔐 Security Considerations

### Data Protection
- Face samples stored locally only
- No cloud upload by default
- Encrypted model file
- Secure authentication flow

### Privacy
- Samples can be deleted after training
- Model file is sufficient for recognition
- No biometric data leaves the system

### Backup
```bash
# Backup trained model
copy engine\auth\trainer\trainer.yml trainer_backup.yml

# Backup samples (optional)
xcopy engine\auth\samples samples_backup\ /E /I
```

---

## 📊 Technical Details

### LBPH Face Recognition

**How it works:**
1. Converts face to grayscale
2. Divides face into small regions
3. Compares local patterns
4. Generates histogram for each region
5. Matches against trained model

**Advantages:**
- Works in varying lighting
- Robust to facial expressions
- Fast recognition
- Low computational requirements

### Haar Cascade Detection

**Purpose:** Detect face location in image

**Process:**
1. Scans image with sliding window
2. Applies cascade of classifiers
3. Identifies face regions
4. Returns coordinates

---

## 🆘 Common Issues

### Issue: "Module not found: cv2"
**Solution:**
```bash
pip install opencv-python opencv-contrib-python
```

### Issue: "Trainer file not found"
**Solution:**
Run trainer.py first:
```bash
python engine/auth/trainer.py
```

### Issue: "No samples found"
**Solution:**
Run sample.py first:
```bash
python engine/auth/sample.py
```

### Issue: "Camera permission denied"
**Solution:**
- Windows Settings → Privacy → Camera
- Allow desktop apps to access camera

---

## 🎓 Advanced Configuration

### Multi-Face Detection

Enable detection of multiple faces:

```python
# In recoganize.py
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(int(minW), int(minH))
)
```

### Custom Training Parameters

```python
# In trainer.py
recognizer = cv2.face.LBPHFaceRecognizer_create(
    radius=1,
    neighbors=8,
    grid_x=8,
    grid_y=8
)
```

---

## 📞 Support

For face recognition issues:
- Check camera is working in other apps
- Verify all files are present
- Review error messages carefully
- Ensure good lighting conditions

---

**Vishwakarma AI - Secure Face Authentication**

*Crafting Intelligence, Building Solutions*

© 2025 Vishwakarma Industries. All rights reserved.
