import pyttsx3 #python text to speech convertor
import speech_recognition as sr #importing speech recognition package from google api
import datetime #to deal with date and time
import wikipedia #pip install wikipedia
import webbrowser #​to control browser operations
import os #provides functions for interacting with the o.s
import sys #to manipulate different parts of python runtime environment
import random #generating random element
import wolframalpha #to calculate strings into formula, its a website which provides api, 100 times per day​
import re #used for string searching and manipulation
import pyjokes #fetch your jokes in python

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client("WA2PYE-7R9TGE328E")
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 4000
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User said: ' + query + '\n')
    
    except Exception as e:
        print(e)
        speak("Your last command couldn​\'​t be heard​ my lord.pleaze repeat again")
        print("Repeat plz")
        return "None"
      
    return query


def wishMe():
    speak("what's your name, human?")
    name=takeCommand()
    speak("hello,"+name+".")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")   

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "define yourself" in query or "who are you" in query:
              speak('''Hello, I am JArvis. Your personal Assistant.​I am here to make your life easier. 
                     You can command me to perform various tasks such as calculating sums or opening applications etcetra​''')
        
        elif "created" in query or "who made you" in query:
             speak("MY life is made by my lord ROHIT RKx")
        
        elif 'youtube' in query:
            speak("okay")
            if('search' not in query):
                     webbrowser.get('firefox').open("youtube.com")
            else:
                new=2
                url="https://www.youtube.com/results?search_query="
                query=str(query).split(' ')
                print(query)
                term=" "
                if 'search' in query:
                     new=2
                     url="https://www.youtube.com/results?search_query="
                     for i in query:
                            if i!="search" and i!="youtube":
                                  term=term+" "+i
                     webbrowser.open(url+term,new=new)

        elif "joke" in query:
            x=pyjokes.get_joke()
            print(x)
            speak(pyjokes.get_joke())

        elif 'open google' in query:
            speak("okay")
            webbrowser.get('firefox').open("google.com")

        elif "what\'s up" in query or 'how are you' in query or "how is your day going on" in query :
            stMsgs = ['Just doing my thingst!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(stMsgs)

        elif 'play' and  'music' in query:
            music_dir = 'D:\\#Maaz mp3\\VA Top Songs of 2017'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak('Okay, here is your music! Enjoy!')

        elif "open website" in query:
             reg_ex=re.search('open website (.+)',query)
             if reg_ex:
                 domain=reg_ex.group(1)
                 url='http://www.'+domain
                 webbrowser.open(url)
                 print("done")
        
        elif 'the time' in query or 'date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            dt=datetime.datetime.now().strftime("And it is %A the %dth of %B %Y") 
            speak(f"Sir, the time is {strTime}")
            speak(f"{dt}")
       
        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        
        else:
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('according to WOLFRAM-ALPHA - ')
                print(results)
                speak('the,answer is'+results)
                    
            except:
                speak("i can search the web for you.Just wait")
                new=2
                url="https://www.google.com/search?client=firefox-b-d&q="
                term=query
                webbrowser.open(url+term,new=new)
               
         
        speak('Next Command! Sir!')