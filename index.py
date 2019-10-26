import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

muzic = 0

def speaks(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speaks('Good Morning!!!')
    elif hour >= 12 and hour <18:
        speaks('Good Afternoon!!!')
    else:
        speaks('Good Evening!!!')

    speaks('Jarvis listining, How can i help u')

def takecommand() :
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognising....')
        speaks('recognising....')
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query} \n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        speaks("say that again please...")
        return "None"
    return query    

if __name__  == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'search' in query:
            speaks('Searching...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            # speaks("According to wiki")
            print(results)
            speaks(results)
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'the time' in query:
            srttime = datetime.datetime.now().strftime("%H:%M:%S")
            speaks(f"Sir, cuurent time is {srttime}")

        elif 'open visual' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play music' in query:
            music_dir = "D:\\music"
            print(f"music_dir : {music_dir}\n")                
            songs = os.listdir(music_dir)
            print(f"songs {songs}\n")
            os.startfile(os.path.join(music_dir, songs[muzic]))
            # PLAYERPATH = "C:\Program Files (x86)\Windows Media Player/wmplayer.exe"
            # subprocess.call([PLAYERPATH, os.path.join(music_dir, songs[muzic])])

        elif 'next song' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            muzic = muzic + 1
            print(f"list of songs {muzic}\n")
            print(songs[muzic])
            if len(songs) == muzic:
                muzic = 0
                os.startfile(os.path.join(music_dir, songs[muzic]))
            else:
                os.startfile(os.path.join(music_dir, songs[muzic]))

        elif 'first song' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            muzic = muzic + 1
            print(f"list of songs {muzic}\n")
            print(songs[muzic])
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'power off' in query:
            speaks('Jarvis Shutting down....')
            exit()

        elif 'terminal' in query:
            os.startfile("c:\\windows\\system32\\cmd.exe")
