import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import psutil
import os
import pyautogui
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time


engine = pyttsx3.init()
wolframalpha_app_id = '8UALYE-X7AW8G4X25'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")#for 24 hrs clock
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back !")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir !")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir !")
    else:
        speak("Good Night !")
    speak("Jarvis at your service. Please tell me how can i help you today sir ?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 50
        r.dynamic_energy_threshold = False
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...... Or Try typing the command!")
        query = str(input('Command: '))
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/lords/Desktop/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

if __name__=="__main__":

    wishme()

    while True:
        query = TakeCommand().lower()
        #All commands wiil be stored in lower case in query
        #for easy recognition

        if 'time' in query: #tell us time when asked' #tell us time when asked
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia'in query:
            speak("Searching.........")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'search in firefox' in query:
            speak('what should I search?')
            firefoxpath = 'C:\Program Files\Mozilla Firefox\firefox.exe %s'

            search = TakeCommand().lower()
            wb.get(firefoxpath).open_new_tab(search='.com')#only open websites with '.com' at end

        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Here We go to Youtube !")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()
    
        elif 'go offline' in query:
            speak('Going offline sir')
            quit()

        elif 'word' in query:
            speak('Opening Word........')
            ms_word = r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I write, sir ?")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir should I include Date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'ok' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                files.write(notes)
                speak('Done Taking Notes, sir')
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that" +memory)
            with open('memory.txt', 'a') as remember:
                remember.write(memory)

        elif 'do you remember anything' in query:
            remember = open('memory.txt' , r)
            speak('You asked me to remember that'+remember.read())
        
        elif 'news' in query:
            try:
                jsonObj =urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=58eabd59e5384acab0d93bd22ce787b9")
                data = json.load(jsonObj)
                i = i

                speak('Here are some top headlines for techcrunch for you, sir')
                print('========TECHCRUNCH HEADLINES========'+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))
    
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)


        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx +1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is: '+answer)
            speak('The Answer is'+answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
            
        elif 'stop listening' in query:
            speak('For  How many seconds you want me to stop listening to your commands, sir ?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
input()            
