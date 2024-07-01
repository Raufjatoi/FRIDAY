import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import os
import requests
import wikipedia

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for hotword and activate assistant
def listen_for_hotword():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for hotword...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")
                if "friday" in command:
                    activate_assistant()
            except sr.UnknownValueError:
                continue

# Function to activate assistant and process commands
def activate_assistant():
    speak("FRIDAY is activated")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for commands...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")
                if "deactivate" in command or "bye" in command:
                    speak("Okay, deactivating for now. Call me again if you need me.")
                    break
                elif "hi friday" in command or "hi" in command or "hello friday" in command:
                    speak(random.choice(["Hey there", "Hello, how are you?", "Hi!"]))
                elif "how are you" in command:
                    speak("I'm just a computer program, so I don't have feelings, but I'm here to help you!")
                elif "who are you" in command:
                    speak("I am FRIDAY, your personal assistant.")
                elif "tell me something" in command:
                    speak("Sure, tell me what to say.")
                    while True:
                        audio = recognizer.listen(source)
                        try:
                            response = recognizer.recognize_google(audio).lower()
                            print(f"You said: {response}")
                            speak(response)
                            break
                        except sr.UnknownValueError:
                            speak("Sorry, I didn't catch that. Could you repeat?")
                            continue
                elif "search for" in command:
                    search_query = command.replace("search for", "").strip()
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Searching Google for: {search_query}")
                elif "what is" in command or "who is" in command or "how" in command:
                    if "search" in command:
                        search_query = command.split("search")[1].strip()
                        url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open(url)
                        speak(f"Searching Google for: {search_query}")
                    else:
                        try:
                            search_query = command.replace("what is", "").replace("who is", "").replace("how", "").strip()
                            result = wikipedia.summary(search_query, sentences=2)
                            speak(result)
                        except wikipedia.exceptions.DisambiguationError as e:
                            speak("There are multiple results for this query, please be more specific.")
                        except wikipedia.exceptions.PageError:
                            speak("I couldn't find any information on that topic.")
                elif "play music" in command:
                    play_music()
                elif "play movie" in command:
                    play_movie()
                elif "play game" in command:
                    play_game()
                elif "news" in command:
                    get_news()
                elif "thanks" in command or "thank you" in command:
                    speak("You're welcome!")
                else:
                    speak("Sorry, I didn't understand that command.")
            except sr.UnknownValueError:
                continue

# Function to play music
def play_music():
    speak("Enjoy the music!")
    music_folder = r"D:\Music\music\Multiply (x)"  # Update with your music folder path
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    try:
        os.startfile(music_path)  # Open the music file with default application
    except FileNotFoundError:
        speak("Sorry, I couldn't find any music.")

# Function to play movie
def play_movie():
    speak("Enjoy the movie!")
    movie_folder = r"D:\Videos\movs"  # Update with your movies folder path
    movie_files = os.listdir(movie_folder)
    random_movie = random.choice(movie_files)
    movie_path = os.path.join(movie_folder, random_movie)
    try:
        os.startfile(movie_path)  # Open the movie file with default application
    except FileNotFoundError:
        speak("Sorry, I couldn't find any movies.")

# Function to play game
def play_game():
    speak("Of course! Which game would you like to play? Tic Tac Toe or Rock Paper Scissors?")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            if "tic tac toe" in command:
                speak("Let's play Tic Tac Toe!")
                # Add your Tic Tac Toe game logic here
            elif "rock paper scissors" in command:
                speak("Let's play Rock Paper Scissors!")
                # Add your Rock Paper Scissors game logic here
            else:
                speak("Sorry, I didn't understand that. Please say Tic Tac Toe or Rock Paper Scissors.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please say Tic Tac Toe or Rock Paper Scissors.")

# Function to fetch and speak news
def get_news():
    speak("Fetching the latest news.")
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"  # Replace with your News API key
    response = requests.get(url).json()
    articles = response["articles"]
    for article in articles[:5]:  # Get top 5 news
        speak(article["title"])

# Start listening for hotword
if __name__ == "__main__":
    listen_for_hotword()
