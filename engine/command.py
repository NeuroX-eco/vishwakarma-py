"""
Vishwakarma AI - Command Processing Module
© 2025 Vishwakarma Industries

This module handles speech recognition, text-to-speech, and command processing.
"""
import os
import time
import requests
import speech_recognition as sr
import pyttsx3
import eel
from playsound import playsound
from engine.config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

def speak(text):
    """
    Text-to-speech using ElevenLabs API with fallback to pyttsx3.

    Args:
        text (str): The text to be spoken.
    """
    text = str(text)
    eel.DisplayMessage(text)
    eel.receiverText(text)

    if not ELEVENLABS_API_KEY:
        print("ElevenLabs API key not configured. Using fallback TTS.")
        fallback_speak(text)
        return

    try:
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
        response.raise_for_status()

        audio_file = "www/assets/audio/temp_speech.mp3"
        os.makedirs(os.path.dirname(audio_file), exist_ok=True)

        with open(audio_file, 'wb') as f:
            f.write(response.content)

        playsound(audio_file)

        try:
            os.remove(audio_file)
        except OSError as e:
            print(f"Error removing temp audio file: {e}")

    except requests.exceptions.RequestException as e:
        print(f"ElevenLabs API Error: {e}")
        fallback_speak(text)
    except Exception as e:
        print(f"An unexpected error occurred in speak function: {e}")
        fallback_speak(text)

def fallback_speak(text):
    """Fallback TTS using pyttsx3."""
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 174)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Fallback TTS Error: {e}")

def takecommand():
    """
    Recognizes speech using the Google Web Speech API.

    Returns:
        str: The recognized command in lowercase, or an empty string if recognition fails.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            time.sleep(2)
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return ""

@eel.expose
def allCommands(message=None):
    """
    Processes all voice or text commands.

    Args:
        message (str, optional): A text command. If None, listens for a voice command.
    """
    query = message if message else takecommand()
    eel.senderText(query)

    if not query or not query.strip():
        print("Empty query received")
        eel.ShowHood()
        return

    try:
        process_command(query)
    except Exception as e:
        print(f"Error processing command: {e}")
        speak("Sorry, I encountered an error processing your request.")
    finally:
        eel.ShowHood()

def process_command(query):
    """
    Determines the type of command and calls the appropriate function.

    Args:
        query (str): The command to be processed.
    """
    from engine.features import (openCommand, PlayYoutube, findContact,
                                 whatsApp, makeCall, sendMessage, chatBot)

    if "open" in query:
        openCommand(query)
    elif "on youtube" in query:
        PlayYoutube(query)
    elif any(keyword in query for keyword in ["send message", "phone call", "video call"]):
        handle_communication_command(query, findContact, whatsApp, makeCall, sendMessage)
    else:
        chatBot(query)

def handle_communication_command(query, findContact, whatsApp, makeCall, sendMessage):
    """
    Handles communication-related commands (WhatsApp, call, SMS).

    Args:
        query (str): The user's command.
        findContact (function): Function to find a contact.
        whatsApp (function): Function to interact with WhatsApp.
        makeCall (function): Function to make a phone call.
        sendMessage (function): Function to send an SMS.
    """
    contact_no, name = findContact(query)
    if not contact_no:
        return

    speak("Which mode would you like to use: WhatsApp or mobile?")
    preference = takecommand()
    print(preference)

    if "mobile" in preference:
        if "send message" in query or "send sms" in query:
            speak("What message would you like to send?")
            message = takecommand()
            sendMessage(message, contact_no, name)
        elif "phone call" in query:
            makeCall(name, contact_no)
        else:
            speak("Please try again.")
    elif "whatsapp" in preference:
        if "send message" in query:
            speak("What message would you like to send?")
            message_content = takecommand()
            whatsApp(contact_no, message_content, 'message', name)
        elif "phone call" in query:
            whatsApp(contact_no, "", 'call', name)
        else:
            whatsApp(contact_no, "", 'video call', name)
    else:
        speak("Invalid mode selected. Please try again.")
