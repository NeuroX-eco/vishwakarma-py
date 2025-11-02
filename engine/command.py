"""
Vishwakarma AI - Command Processing Module
© 2025 Vishwakarma Industries
"""

import speech_recognition as sr
import eel
import time
import requests
import os
from playsound import playsound
from engine.config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

def speak(text):
    """Text-to-speech using ElevenLabs API with fallback to pyttsx3"""
    text = str(text)
    eel.DisplayMessage(text)
    eel.receiverText(text)
    
    # Check if API key is available
    if not ELEVENLABS_API_KEY:
        print("ElevenLabs API key not configured. Using fallback TTS.")
        fallback_speak(text)
        return
    
    try:
        # Use ElevenLabs TTS
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
        
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
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
        
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            # Save audio to temp file
            audio_file = "www/assets/audio/temp_speech.mp3"
            os.makedirs(os.path.dirname(audio_file), exist_ok=True)
            
            with open(audio_file, 'wb') as f:
                f.write(response.content)
            
            # Play audio
            playsound(audio_file)
            
            # Clean up temp file
            try:
                os.remove(audio_file)
            except:
                pass
        elif response.status_code == 401:
            print("ElevenLabs API Error: Invalid API key (401 Unauthorized)")
            fallback_speak(text)
        elif response.status_code == 429:
            print("ElevenLabs API Error: Rate limit exceeded (429). Using fallback.")
            fallback_speak(text)
        else:
            print(f"ElevenLabs TTS Error: {response.status_code} - {response.text}")
            fallback_speak(text)
            
    except requests.exceptions.Timeout:
        print("ElevenLabs API Error: Request timeout. Using fallback TTS.")
        fallback_speak(text)
    except requests.exceptions.ConnectionError:
        print("ElevenLabs API Error: Connection failed. Check your internet connection.")
        fallback_speak(text)
    except Exception as e:
        print(f"TTS Error: {e}")
        fallback_speak(text)

def fallback_speak(text):
    """Fallback TTS using pyttsx3"""
    try:
        import pyttsx3
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 174)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Fallback TTS Error: {e}")


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    except Exception as e:
        print(f"Error in speech recognition: {e}")
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    # Check if query is empty
    if not query or query.strip() == "":
        print("Empty query received")
        eel.ShowHood()
        return
    
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)

        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as e:
        print(f"Error processing command: {e}")
        speak("Sorry, I encountered an error processing your request")
    
    eel.ShowHood()