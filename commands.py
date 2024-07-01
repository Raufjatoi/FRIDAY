# commands.py

import webbrowser
import random
import os
import wikipedia
import requests

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_wikipedia(query):
    return wikipedia.summary(query, sentences=2)

def play_music(music_folder):
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    try:
        os.startfile(music_path)
    except FileNotFoundError:
        return "Sorry, I couldn't find any music."
    return "Enjoy the music!"

def play_movie(movie_folder):
    movie_files = os.listdir(movie_folder)
    random_movie = random.choice(movie_files)
    movie_path = os.path.join(movie_folder, random_movie)
    try:
        os.startfile(movie_path)
    except FileNotFoundError:
        return "Sorry, I couldn't find any movies."
    return "Enjoy the movie!"

def get_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()
    articles = response["articles"]
    news = [article["title"] for article in articles[:5]]
    return news
