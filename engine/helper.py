"""
Vishwakarma AI - Helper Utilities Module
© 2025 Vishwakarma Industries

This module provides helper functions for various tasks.
"""
import os
import re
import time
import subprocess

def extract_yt_term(command):
    """
    Extracts the search term from a 'play on YouTube' command.

    Args:
        command (str): The user's command.

    Returns:
        str: The extracted search term, or None if not found.
    """
    match = re.search(r'play\s+(.*?)\s+on\s+youtube', command, re.IGNORECASE)
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    """
    Removes specified words from a string.

    Args:
        input_string (str): The string to process.
        words_to_remove (list): A list of words to remove.

    Returns:
        str: The string with the specified words removed.
    """
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    return ' '.join(filtered_words)


def run_adb_command(command):
    """
    Executes an ADB command and handles potential errors.

    Args:
        command (str): The ADB command to execute.
    """
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        time.sleep(1)
    except subprocess.CalledProcessError as e:
        print(f"ADB command failed: {e.stderr}")
    except FileNotFoundError:
        print("ADB not found. Please ensure it's installed and in your system's PATH.")


def keyEvent(key_code):
    """
    Sends a key event to the connected Android device.

    Args:
        key_code (int): The key code to send.
    """
    run_adb_command(f'adb shell input keyevent {key_code}')


def tapEvents(x, y):
    """
    Simulates a tap event at the specified coordinates.

    Args:
        x (int): The x-coordinate.
        y (int): The y-coordinate.
    """
    run_adb_command(f'adb shell input tap {x} {y}')


def adbInput(message):
    """
    Sends a text input to the connected Android device.

    Args:
        message (str): The text to send.
    """
    escaped_message = message.replace('"', '\\"')
    run_adb_command(f'adb shell input text "{escaped_message}"')


def goback(times=6):
    """
    Simulates pressing the back button multiple times.

    Args:
        times (int): The number of times to press the back button.
    """
    for _ in range(times):
        keyEvent(4)  # Key code for the back button is 4


def replace_spaces_with_percent_s(input_string):
    """
    Replaces spaces in a string with '%s'.

    Args:
        input_string (str): The string to process.

    Returns:
        str: The modified string.
    """
    return input_string.replace(' ', '%s')
