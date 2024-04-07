import pyttsx3
import datetime
import speech_recognition as sr
import  wikipedia
import webbrowser
import os
import random

# code for making jarvis speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello!")
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("i am jarvis")
    speak("How can i help you today")

# code for recognising speech
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...\n")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wilipedia","")
            results = wikipedia.summary(query,sentences=2) 
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsap.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\mdd15\\Downloads\\music_dir"
            songs = os.listdir(music_dir)
            song_no = random.randint(0,len(songs))
            
            print(songs)
            os.startfile(os.path.join(music_dir,songs[song_no]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        