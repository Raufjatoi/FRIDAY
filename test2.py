import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import subprocess
import os

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
                elif "hi friday" in command:
                    speak(random.choice(["Hey there", "Hello, how are you?", "Hi!"]))
                elif "hi" in command:
                    speak(random.choice(["Hey there", "Hello, how are you?", "Hi!"]))
                elif "hello friday" in command:
                    speak(random.choice(["Hey there", "Hello, how are you?", "Hi!"]))
                elif "tell me something" in command:
                    speak("Sure, tell me what to say.")
                    continue_listening = True
                    while continue_listening:
                        audio = recognizer.listen(source)
                        try:
                            response = recognizer.recognize_google(audio).lower()
                            print(f"You said: {response}")
                            speak(response)
                            continue_listening = False
                        except sr.UnknownValueError:
                            speak("Sorry, I didn't catch that. Could you repeat?")
                            continue
                elif "what is" in command or "search for" in command:
                    search_query = command.replace("what is", "").replace("search for", "").strip()
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Searching Google for: {search_query}")
                elif "who is" in command or "search for" in command:
                    search_query = command.replace("what is", "").replace("search for", "").strip()
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Searching Google for: {search_query}")
                elif "how " in command or "search for" in command:
                    search_query = command.replace("what is", "").replace("search for", "").strip()
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Searching Google for: {search_query}")
                
                elif "play music" in command:
                    play_music()
                elif "play some movie" in command:
                    play_movie()
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

# Start listening for hotword
if __name__ == "__main__":
    listen_for_hotword()
