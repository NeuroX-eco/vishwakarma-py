"""
Vishwakarma AI - Core Features Module
© 2025 Vishwakarma Industries

This module contains the core features of the Vishwakarma AI assistant.
"""

import os
import sqlite3
import subprocess
import time
import webbrowser
from pipes import quote
from datetime import datetime

import eel
import pyautogui
import pywhatkit as kit
from openai import OpenAI
from playsound import playsound

from engine.command import speak
from engine.config import ASSISTANT_NAME, NVIDIA_API_KEY, NVIDIA_MODEL
from engine.helper import (adbInput, extract_yt_term, goback, keyEvent,
                           remove_words, replace_spaces_with_percent_s,
                           tapEvents)

# Database connection
try:
    con = sqlite3.connect("vishwakarma.db")
    cursor = con.cursor()
except sqlite3.Error as e:
    print(f"Database connection error: {e}")
    # Handle the error gracefully, maybe by disabling database-dependent features
    con = None
    cursor = None

@eel.expose
def playAssistantSound():
    """Plays the assistant's startup sound."""
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    try:
        playsound(music_dir)
    except Exception as e:
        print(f"Error playing sound: {e}")

def openCommand(query):
    """
    Opens applications, websites, or system commands based on the query.

    Args:
        query (str): The user's command.
    """
    app_name = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()

    if not app_name:
        speak("Please specify what to open.")
        return

    if not cursor:
        speak("Database not connected. Cannot open commands.")
        return

    try:
        # Check for system commands
        cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (app_name,))
        sys_results = cursor.fetchall()
        if sys_results:
            speak(f"Opening {app_name}")
            os.startfile(sys_results[0][0])
            return

        # Check for web commands
        cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (app_name,))
        web_results = cursor.fetchall()
        if web_results:
            speak(f"Opening {app_name}")
            webbrowser.open(web_results[0][0])
            return

        # Fallback to system command
        speak(f"Opening {app_name}")
        os.system(f'start {app_name}')

    except Exception as e:
        print(f"Error in openCommand: {e}")
        speak(f"Sorry, I couldn't open {app_name}. Application not found.")


def PlayYoutube(query):
    """
    Plays a YouTube video based on the query.

    Args:
        query (str): The user's command.
    """
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on YouTube")
    kit.playonyt(search_term)


def findContact(query):
    """
    Finds a contact in the database.

    Args:
        query (str): The name of the contact to find.

    Returns:
        tuple: A tuple containing the mobile number and the contact's name,
               or (None, None) if not found.
    """
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    contact_name = remove_words(query, words_to_remove).strip().lower()

    if not cursor:
        speak("Database not connected. Cannot find contacts.")
        return None, None

    try:
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ?", (f'%{contact_name}%',))
        results = cursor.fetchall()

        if not results:
            speak('Contact not found in your list.')
            return None, None

        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = f'+91{mobile_number_str}'

        return mobile_number_str, contact_name
    except Exception as e:
        print(f"Error finding contact: {e}")
        speak('Error accessing contacts.')
        return None, None


def whatsApp(mobile_no, message, flag, name):
    """
    Sends a WhatsApp message, or initiates a voice or video call.

    Args:
        mobile_no (str): The recipient's mobile number.
        message (str): The message to send.
        flag (str): The action to perform ('message', 'call', or 'video_call').
        name (str): The name of the contact.
    """
    actions = {
        'message': {'tab': 12, 'message': f"Message sent successfully to {name}"},
        'call': {'tab': 7, 'message': f"Calling {name}"},
        'video_call': {'tab': 6, 'message': f"Starting video call with {name}"}
    }

    action = actions.get(flag)
    if not action:
        speak("Invalid WhatsApp action.")
        return

    encoded_message = quote(message if flag == 'message' else "")
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    try:
        subprocess.run(full_command, shell=True, check=True)
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'f')
        for _ in range(action['tab']):
            pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        speak(action['message'])
    except subprocess.CalledProcessError as e:
        print(f"Error opening WhatsApp: {e}")
        speak("Failed to open WhatsApp.")
    except Exception as e:
        print(f"An unexpected error occurred in whatsApp: {e}")
        speak("An unexpected error occurred.")


def chatBot(query):
    """
    AI chatbot using NVIDIA API with comprehensive error handling.

    Args:
        query (str): The user's input.

    Returns:
        str: The chatbot's response.
    """
    user_input = query.strip()
    if not user_input:
        speak("I didn't catch that. Could you please repeat?")
        return

    if not NVIDIA_API_KEY:
        print("NVIDIA API key not configured. Using fallback chatbot.")
        return fallback_chatbot(user_input)

    try:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=NVIDIA_API_KEY
        )

        print(f"Sending to NVIDIA AI: {user_input}")

        completion = client.chat.completions.create(
            model=NVIDIA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are Vishwakarma AI, an intelligent voice assistant. Keep responses brief and conversational."
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=200,
            stream=False
        )

        response = completion.choices[0].message.content
        print(f"NVIDIA AI response: {response}")
        speak(response)
        return response

    except Exception as e:
        error_msg = str(e).lower()
        if "401" in error_msg or "unauthorized" in error_msg:
            print("NVIDIA API Error: Invalid API key (401 Unauthorized)")
        elif "429" in error_msg or "rate limit" in error_msg:
            print("NVIDIA API Error: Rate limit exceeded (429)")
        elif any(err in error_msg for err in ["timeout", "connection"]):
            print("NVIDIA API Error: Network issue")
        else:
            print(f"NVIDIA API error: {e}")

        return fallback_chatbot(user_input)


def fallback_chatbot(query):
    """
    Fallback responses when the API is unavailable.

    Args:
        query (str): The user's input.

    Returns:
        str: The fallback response.
    """
    query = query.lower()
    
    responses = {
        'hello': "Hello! How can I assist you today?",
        'hi': "Hello! How can I assist you today?",
        'hey': "Hello! How can I assist you today?",
        'how are you': "I'm functioning well, thank you for asking! How can I help you?",
        'your name': "I am Vishwakarma AI, your intelligent voice assistant.",
        'who are you': "I am Vishwakarma AI, your intelligent voice assistant.",
        'time': f"The current time is {datetime.now().strftime('%I:%M %p')}",
        'date': f"Today is {datetime.now().strftime('%B %d, %Y')}",
        'thank': "You're welcome! Happy to help.",
        'bye': "Goodbye! Have a great day!",
        'goodbye': "Goodbye! Have a great day!"
    }

    for keyword, response in responses.items():
        if keyword in query:
            print(f"Fallback response: {response}")
            speak(response)
            return response

    default_response = "I understand. How else can I assist you?"
    print(f"Fallback response: {default_response}")
    speak(default_response)
    return default_response


def makeCall(name, mobileNo):
    """
    Makes a phone call using ADB.

    Args:
        name (str): The name of the person to call.
        mobileNo (str): The mobile number to call.
    """
    mobileNo_clean = mobileNo.replace(" ", "")
    speak(f"Calling {name}")
    command = f'adb shell am start -a android.intent.action.CALL -d tel:{mobileNo_clean}'
    os.system(command)


def sendMessage(message, mobileNo, name):
    """
    Sends an SMS message using ADB.

    Args:
        message (str): The message to send.
        mobileNo (str): The recipient's mobile number.
        name (str): The recipient's name.
    """
    message_formatted = replace_spaces_with_percent_s(message)
    mobileNo_formatted = replace_spaces_with_percent_s(mobileNo)
    speak("Sending message")

    try:
        goback(4)
        time.sleep(1)
        keyEvent(3)
        # Open SMS app
        tapEvents(136, 2220)
        # Start chat
        tapEvents(819, 2192)
        # Search mobile no
        adbInput(mobileNo_formatted)
        # Tap on name
        tapEvents(601, 574)
        # Tap on input
        tapEvents(390, 2270)
        # Message
        adbInput(message_formatted)
        # Send
        tapEvents(957, 1397)
        speak(f"Message sent successfully to {name}")
    except Exception as e:
        print(f"Error sending message via ADB: {e}")
        speak("Failed to send the message.")
