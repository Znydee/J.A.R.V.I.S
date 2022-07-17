import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Zarif!")

    elif hour>=12 and hour<18:
        speak("Good afternoon Zarif!")   

    else:
        speak("Good evening Zarif!")  

    speak("I am on, jarvis mode activated.")       

def take_command():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Kindly Say that again please...")  
        return "None"
    return query


def reminder():
    speak("what reminder do you want to set Zarif ?")
    reminder_name= take_command()
    speak("what time do you want to be reminded ?")# something like 1:00am 1:30pm...
    set_reminder= take_command()
    if len(set_reminder)==6:
        set_reminder = "0" + set_reminder
    set_reminder_end= set_reminder[-2:].lower()
    if set_reminder_end == "pm":
        set_reminder_hr = int(set_reminder[0:2]) + 12
        set_reminder_min = int(set_reminder[3:5])
        new_set_reminder = str(set_reminder_hr) +":" + str(set_reminder_min)
    else :
        if set_reminder[0:2] == "12":
            new_set_reminder= "00" + ":" + set_reminder[3:5]
        else:
            new_set_reminder= set_reminder[0:5]
    print(new_set_reminder)
    while True:
        if new_set_reminder == datetime.datetime.now().strftime("%H:%M"):
            print(f"hi zarif, its time for {reminder_name}")
            break
        else:
            pass

if __name__ == "__main__":
    wishMe()
    take_command()
    while True:
        query=take_command.lower

        #Logic for executing tasks based on query
        if "Saira open wikipedia" in query:
            speak('Activating Wikipedia...')
            query = query.replace('Wikipedia', '')
            results = wikipedia.summary(query, sentences=2)

        elif 'Saira open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'Saira open google' in query:
            webbrowser.open("google.com")

        elif 'Saira open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Zarif, the time is {strTime}")
        elif "set reminder" in query:
            reminder()
        elif 'open code' in query:
            codePath = "E:\\VS CODE\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)