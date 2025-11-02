"""
Vishwakarma AI - Core Features Module
© 2025 Vishwakarma Industries
"""

import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
# Playing assistant sound function
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

con = sqlite3.connect("vishwakarma.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except Exception as e:
                        print(f"Error opening {query}: {e}")
                        speak("Application not found")
        except Exception as e:
            print(f"Error in openCommand: {e}")
            speak("Something went wrong while opening the application")

       

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        
        if len(results) == 0:
            speak('Contact not found in your list')
            return 0, 0
            
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except Exception as e:
        print(f"Error finding contact: {e}")
        speak('Error accessing contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

# NVIDIA AI Chatbot
def chatBot(query):
    """AI chatbot using NVIDIA API with comprehensive error handling"""
    try:
        user_input = query.strip()
        if not user_input:
            speak("I didn't catch that. Could you please repeat?")
            return
        
        # Check if API key is available
        from engine.config import NVIDIA_API_KEY, NVIDIA_MODEL
        
        if not NVIDIA_API_KEY:
            print("NVIDIA API key not configured. Using fallback chatbot.")
            return fallback_chatbot(query)
        
        # Use NVIDIA API for AI responses
        from openai import OpenAI
        
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
                    "content": "You are Vishwakarma AI, an intelligent voice assistant created by Vishwakarma Industries. You are helpful, friendly, and provide concise responses suitable for voice interaction. Keep responses brief and conversational."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=200,  # Keep responses concise for voice
            stream=False
        )
        
        response = completion.choices[0].message.content
        print(f"NVIDIA AI response: {response}")
        speak(response)
        return response
        
    except ImportError as e:
        print(f"OpenAI library not installed: {e}")
        print("Install with: pip install openai")
        return fallback_chatbot(query)
    except Exception as e:
        error_msg = str(e).lower()
        
        if "401" in error_msg or "unauthorized" in error_msg:
            print("NVIDIA API Error: Invalid API key (401 Unauthorized)")
            print("Please check your NVIDIA_API_KEY in the .env file")
        elif "429" in error_msg or "rate limit" in error_msg:
            print("NVIDIA API Error: Rate limit exceeded (429)")
            print("Please wait a moment before trying again")
        elif "timeout" in error_msg:
            print("NVIDIA API Error: Request timeout")
            print("Please check your internet connection")
        elif "connection" in error_msg:
            print("NVIDIA API Error: Connection failed")
            print("Please check your internet connection")
        else:
            print(f"NVIDIA API error: {e}")
        
        return fallback_chatbot(query)

def fallback_chatbot(query):
    """Fallback responses when API is unavailable"""
    query = query.lower()
    
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    if any(word in query for word in greetings):
        response = "Hello! How can I assist you today?"
    elif 'how are you' in query:
        response = "I'm functioning well, thank you for asking! How can I help you?"
    elif 'your name' in query or 'who are you' in query:
        response = "I am Vishwakarma AI, your intelligent voice assistant created by Vishwakarma Industries."
    elif 'time' in query:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"
    elif 'date' in query:
        from datetime import datetime
        current_date = datetime.now().strftime("%B %d, %Y")
        response = f"Today is {current_date}"
    elif 'thank' in query:
        response = "You're welcome! Happy to help."
    elif 'bye' in query or 'goodbye' in query:
        response = "Goodbye! Have a great day!"
    else:
        response = "I understand. How else can I assist you?"
    
    print(f"Fallback response: {response}")
    speak(response)
    return response

# android automation

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)


# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("message send successfully to "+name)