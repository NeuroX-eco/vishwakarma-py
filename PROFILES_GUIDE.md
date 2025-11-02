# Vishwakarma AI - User Profiles Guide

**© 2025 Vishwakarma Industries**

---

## 🎭 User Profiles Feature

Vishwakarma AI now supports multiple user profiles for a personalized experience!

---

## 📋 Features

### Profile Management
- ✅ **Create Multiple Profiles** - Support for multiple users
- ✅ **Personalized Greetings** - Custom welcome messages
- ✅ **User Preferences** - Save individual preferences
- ✅ **Face Recognition Integration** - Link profiles to face authentication
- ✅ **Profile Switching** - Easy switching between users
- ✅ **Last Login Tracking** - Track when users last accessed the system

### Profile Data
Each profile stores:
- User ID (auto-generated)
- Full Name
- Age (optional)
- Preferences (news, weather, reminders)
- Creation timestamp
- Last login timestamp
- Active status

---

## 🚀 Getting Started

### First Time Setup

1. **Launch Vishwakarma AI**
   ```bash
   python run.py
   ```

2. **Create Your Profile**
   - Enter your full name
   - Optionally enter your age
   - Select your preferences:
     - News Updates
     - Weather Updates
     - Reminders

3. **Complete Face Authentication**
   - After profile creation, proceed with face capture
   - Run sample capture: `python engine/auth/sample.py`
   - Train the model: `python engine/auth/trainer.py`

4. **Start Using Vishwakarma AI**
   - Your profile is now linked to your face
   - Receive personalized greetings
   - Enjoy customized experience

---

## 👥 Multiple Users

### Adding New Users

1. Each user should create their own profile
2. Capture face samples with unique user ID
3. Train the model with all users' samples
4. System will recognize and greet each user by name

### Profile Database

Profiles are stored in `vishwakarma.db` in the `profiles` table:

```sql
CREATE TABLE profiles (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    preferences TEXT,
    created_at TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN
)
```

---

## 🔧 Profile Management API

### Create Profile
```python
profile_manager.create_profile(name, age, preferences)
```

### Get Profile
```python
profile = profile_manager.get_profile(user_id)
```

### Update Profile
```python
profile_manager.update_profile(user_id, name="New Name", age=30)
```

### Delete Profile (Soft Delete)
```python
profile_manager.delete_profile(user_id)
```

### Get All Profiles
```python
profiles = profile_manager.get_all_profiles()
```

---

## ⚙️ User Preferences

### Available Preferences

1. **News Updates**
   - Receive daily news briefings
   - Customizable news sources

2. **Weather Updates**
   - Get weather forecasts
   - Location-based updates

3. **Reminders**
   - Set and receive reminders
   - Task management

### Setting Preferences

```python
# Set a preference
profile_manager.set_preference(user_id, "theme", "dark")

# Get a preference
theme = profile_manager.get_preference(user_id, "theme", default="light")
```

---

## 🎨 Personalization

### Personalized Greetings

When you log in, Vishwakarma AI greets you by name:
```
"Hello [Your Name], Welcome back! I am Vishwakarma AI, How can I assist you today?"
```

### Custom Settings

Each user can have:
- Custom voice preferences
- Preferred language
- Notification settings
- Privacy settings

---

## 🔐 Privacy & Security

### Data Protection
- All profile data stored locally
- No cloud synchronization by default
- Face recognition data encrypted
- Secure database access

### Profile Privacy
- Each profile is isolated
- No cross-profile data sharing
- Secure authentication required
- Optional profile password protection

---

## 📊 Profile Statistics

Track your usage:
- Total sessions
- Last login time
- Most used features
- Command history

---

## 🛠️ Advanced Features

### Profile Export/Import

Export your profile:
```python
profile_manager.export_profile(user_id, "backup.json")
```

Import a profile:
```python
profile_manager.import_profile("backup.json")
```

### Profile Backup

Backup all profiles:
```bash
# Backup database
copy vishwakarma.db vishwakarma_backup.db
```

---

## 🐛 Troubleshooting

### Profile Not Found
- Ensure profile was created successfully
- Check database connection
- Verify user_id is correct

### Face Recognition Not Working
- Retrain the model with your face samples
- Ensure good lighting conditions
- Check camera permissions

### Preferences Not Saving
- Verify database write permissions
- Check for database locks
- Restart the application

---

## 📝 Example Usage

### Python API

```python
from engine.profile_manager import ProfileManager

# Initialize
pm = ProfileManager()

# Create profile
user_id = pm.create_profile(
    name="John Doe",
    age=30,
    preferences={
        "news": True,
        "weather": True,
        "reminders": False
    }
)

# Get profile
profile = pm.get_profile(user_id)
print(f"Welcome {profile['name']}!")

# Update preferences
pm.set_preference(user_id, "language", "en")

# Get preference
lang = pm.get_preference(user_id, "language")
```

### JavaScript API (Eel)

```javascript
// Create profile
eel.createProfile(name, age, preferences)(function(response) {
    if (response.success) {
        console.log("Profile created!");
    }
});

// Get all profiles
eel.getProfiles()(function(profiles) {
    profiles.forEach(profile => {
        console.log(profile.name);
    });
});

// Switch profile
eel.switchProfile(user_id)(function(response) {
    if (response.success) {
        console.log("Switched to: " + response.profile.name);
    }
});
```

---

## 🎯 Best Practices

1. **Create Unique Profiles** - One profile per user
2. **Regular Backups** - Backup your profile data
3. **Update Preferences** - Keep preferences current
4. **Secure Your System** - Use face authentication
5. **Clean Old Profiles** - Remove unused profiles

---

## 🔄 Migration from Old Version

If upgrading from a version without profiles:

1. Profiles table will be created automatically
2. Create your profile on first launch
3. Link existing face recognition data
4. No data loss - all features preserved

---

## 📞 Support

For profile-related issues:
- Check the main README.md
- Review troubleshooting section
- Verify database integrity

---

**Vishwakarma AI - Personalized Intelligence**

*Crafting Intelligence, Building Solutions*

© 2025 Vishwakarma Industries. All rights reserved.
