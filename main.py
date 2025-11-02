"""
Vishwakarma AI - Main Application
© 2025 Vishwakarma Industries

This module initializes and runs the Vishwakarma AI application.
"""
import os
import eel
from engine.features import playAssistantSound
from engine.command import speak
from engine.auth.recognize import FaceAuthenticator
from engine.profile_manager import ProfileManager

@eel.expose
def init_app():
    """Initializes the application logic."""
    profile_manager = ProfileManager()
    eel.hideLoader()

    if not profile_manager.has_profiles():
        eel.showProfileCreation()
        speak("Welcome to Vishwakarma AI. Please create your profile to get started.")
        return

    speak("Ready for Face Authentication")
    authenticator = FaceAuthenticator()
    if authenticator.authenticate():
        handle_successful_authentication(profile_manager, authenticator)
    else:
        speak("Face Authentication Failed. Please try again.")

def handle_successful_authentication(profile_manager, authenticator):
    """Handles the logic after a successful face authentication."""
    user_id = authenticator.get_authenticated_user_id()
    profile = profile_manager.get_profile(user_id)

    eel.hideFaceAuth()
    speak("Face Authentication Successful")
    eel.hideFaceAuthSuccess()

    greeting = (f"Hello {profile['name']}, Welcome back! "
                f"I am Vishwakarma AI, How can I assist you today?") \
        if profile else \
        "Hello, Welcome! I am Vishwakarma AI, How can I assist you today?"

    speak(greeting)
    eel.hideStart()
    playAssistantSound()

@eel.expose
def createProfile(name, age, preferences):
    """Creates a new user profile."""
    profile_manager = ProfileManager()
    try:
        user_id = profile_manager.create_profile(name, age, preferences)
        speak(f"Profile created successfully for {name}. "
              "Please proceed with face authentication.")
        eel.hideProfileCreation()
        eel.showFaceAuth()
        return {"success": True, "user_id": user_id}
    except Exception as e:
        speak("Failed to create profile. Please try again.")
        print(f"Error creating profile: {e}")
        return {"success": False, "error": str(e)}

@eel.expose
def getProfiles():
    """Gets all user profiles."""
    return ProfileManager().get_all_profiles()

@eel.expose
def switchProfile(user_id):
    """Switches to a different profile."""
    profile = ProfileManager().get_profile(user_id)
    if profile:
        speak(f"Switching to {profile['name']}'s profile")
        return {"success": True, "profile": profile}
    return {"success": False}

def start():
    """Starts the Vishwakarma AI application."""
    eel.init("www")
    
    playAssistantSound()

    # os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
