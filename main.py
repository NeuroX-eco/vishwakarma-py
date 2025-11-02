"""
Vishwakarma AI - Main Application
© 2025 Vishwakarma Industries
"""

import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize
from engine.profile_manager import ProfileManager

def start():
    
    eel.init("www")
    profile_manager = ProfileManager()

    playAssistantSound()
    
    @eel.expose
    def init():
        eel.hideLoader()
        
        # Check if profiles exist
        if not profile_manager.has_profiles():
            eel.showProfileCreation()
            speak("Welcome to Vishwakarma AI. Please create your profile to get started.")
        else:
            speak("Ready for Face Authentication")
            flag = recoganize.AuthenticateFace()
            if flag == 1:
                user_id = recoganize.get_authenticated_user_id()
                profile = profile_manager.get_profile(user_id)
                
                eel.hideFaceAuth()
                speak("Face Authentication Successful")
                eel.hideFaceAuthSuccess()
                
                if profile:
                    greeting = f"Hello {profile['name']}, Welcome back! I am Vishwakarma AI, How can I assist you today?"
                else:
                    greeting = "Hello, Welcome! I am Vishwakarma AI, How can I assist you today?"
                
                speak(greeting)
                eel.hideStart()
                playAssistantSound()
            else:
                speak("Face Authentication Failed. Please try again.")
    
    @eel.expose
    def createProfile(name, age, preferences):
        """Create a new user profile"""
        try:
            user_id = profile_manager.create_profile(name, age, preferences)
            speak(f"Profile created successfully for {name}. Please proceed with face authentication.")
            eel.hideProfileCreation()
            eel.showFaceAuth()
            return {"success": True, "user_id": user_id}
        except Exception as e:
            speak("Failed to create profile. Please try again.")
            return {"success": False, "error": str(e)}
    
    @eel.expose
    def getProfiles():
        """Get all user profiles"""
        return profile_manager.get_all_profiles()
    
    @eel.expose
    def switchProfile(user_id):
        """Switch to a different profile"""
        profile = profile_manager.get_profile(user_id)
        if profile:
            speak(f"Switching to {profile['name']}'s profile")
            return {"success": True, "profile": profile}
        return {"success": False}
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)