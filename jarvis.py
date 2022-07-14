from datetime import datetime
from http import server
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speech_recognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")
     
    speak("I am Jarvis sir. Please tell me how may i help you")

def takeCommand():
    # It takes microphone input from the user and returns string output.

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"   
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arunishverma@gmail.com', 'Arunish@2001')
    server.sendmail('arunishverma@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")        

        elif 'play music' in query:
            music_dir ='C:\\Users\\aruni\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))   

        elif 'the time' in query:
            strTime =datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")    
        
        elif 'open code' in query:
            codePath = "C:\\Users\\aruni\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to arunish kumar' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to ="arunishverma@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend arunish bhai. i am not able to send this email")    


        # elif 'quit' in query:
        #     print(quit)
        # quit()