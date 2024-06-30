import os
import webbrowser
import pyttsx3
from games import tic_tac_toe, rock_paper_scissors

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    if "play music" in command:
        play_music()
    elif "play movie" in command:
        play_movie()
    elif "close this window" in command:
        close_window()
    elif "what is" in command or "search for" in command:
        google_search(command)
    elif "play tic-tac-toe" in command:
        tic_tac_toe.play()
    elif "play rock-paper-scissors" in command:
        rock_paper_scissors.play()

def play_music():
    speak("Playing music")
    # This will be a placeholder for Spotify API integration
    print("Playing music...")

def play_movie():
    speak("Playing movie")
    # This will be a placeholder for VLC or Pygame integration
    print("Playing movie...")

def close_window():
    speak("Closing the window")
    # Placeholder for closing the window
    print("Closing the window...")

def google_search(query):
    search_query = query.replace("what is", "").replace("search for", "").strip()
    url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(url)
    speak(f"Searching Google for: {search_query}")
    print(f"Searching Google for: {search_query}")
