import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
from datetime import datetime
import subprocess as sp
import os

from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def greet_user():
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"Debjyoti: {user_input}")
            return user_input.lower()
        except sr.UnknownValueError:
            speak("Sorry did not understand what you just said. Try again")
            return ""
        
def chrome_search(user_command):
    search_term = user_command.replace("search", "").strip()
    search_url = f"https://www.google.com/search?q={search_term}"
    webbrowser.open(search_url)
    speak(f"Opening Chrome and searching: {search_term}")

def play_youtube(user_command):
    search_term = user_command.replace("play", "")
    pywhatkit.playonyt(search_term)

def youtube_search(user_command):
    search_query = user_command.split('youtube', 1)[1].strip()
    print(f"Searching YouTube for: {search_query}")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen("C:\\Windows\\System32\\calc.exe")