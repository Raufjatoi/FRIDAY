import speech_recognition as sr
import pyttsx3
import random
from commands import execute_command

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
                if "deactivate" in command:
                    speak("Okay Rauf, deactivating")
                    break
                elif "hi friday" in command:
                    speak(random.choice(["Hey Rauf", "Hi Rauf, how are you?", "Hello Rauf, how's your day?", "Hi"]))
                else:
                    execute_command(command)
            except sr.UnknownValueError:
                continue
