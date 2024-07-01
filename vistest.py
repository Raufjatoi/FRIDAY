
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import os
import requests
import wikipedia
import cv2

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
                    play_music_with_gesture()
                elif "play movie" in command:
                    play_movie_with_gesture()
                elif "play game" in command:
                    play_game()
                elif any(word in command for word in ["news", "latest news", "headlines"]):
                    get_news()
                elif "thanks" in command or "thank you" in command:
                    speak("You're welcome!")
                else:
                    speak("Sorry, I didn't understand that command.")
            except sr.UnknownValueError:
                continue

# Function to play music with gesture recognition
def play_music_with_gesture():
    speak("Starting music playback. Show one finger to play or pause.")
    cap = cv2.VideoCapture(0)
    gesture = None

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.rectangle(frame, (200, 200), (400, 400), (255, 0, 0), 2)
        roi = frame[200:400, 200:400]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(max_contour)
            if area > 2000:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x + 200, y + 200), (x + 200 + w, y + 200 + h), (0, 255, 0), 2)
                if w > 100 and h > 100:
                    gesture = "pause" if gesture != "pause" else "play"
                    speak(f"Seen {gesture} motion, {gesture}...")
                    break

        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to play movie with gesture recognition
def play_movie_with_gesture():
    speak("Starting movie playback. Show one finger to play or pause.")
    cap = cv2.VideoCapture(0)
    gesture = None

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.rectangle(frame, (200, 200), (400, 400), (255, 0, 0), 2)
        roi = frame[200:400, 200:400]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(max_contour)
            if area > 2000:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x + 200, y + 200), (x + 200 + w, y + 200 + h), (0, 255, 0), 2)
                if w > 100 and h > 100:
                    gesture = "pause" if gesture != "pause" else "play"
                    speak(f"Seen {gesture} motion, {gesture}...")
                    break

        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

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
