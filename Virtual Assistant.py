import pyttsx3
import sys
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import subprocess
import time
import random
from gtts import gTTS
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#def speak(audioString):
    #engine.say(audioString)
    #print("user said:",audioString)
    #engine.runAndWait()
    #my_obj = gTTS(audioString, tld='com',lang='en',slow=False,lang_check=True)
    #my_obj.save("audio.mp3")
    #os.system("mpg123 audio.mp3")

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir!')

    elif hour >= 12 and hour < 17:
        speak('Good AfterNoon Sir!')

    else:
        speak('Good Evening Sir!')

    #speak("I'm Friday. How may i help you.")

def record():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1, sample_rate=None, chunk_size=1024)

    with mic as source:
        print('Listening....')
        #r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source,duration=1)
        r.energy_threshold = 4000
        #r.operation_timeout = None
        #r.phrase_threshold = 0.5
        #r.non_speaking_duration = 0.5
        r.dynamic_energy_ratio = 1.5
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        audio = r.listen(source)
        query = ""
        try:
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-In')
            print(f'You said:{query}\n')


        except Exception as e:
            print('Say that again please...')
            #return 'None'
        return query

def taskExecution(query):

    #wishMe()
    while True:
        query = record().lower()

        if 'what is the time' in query or "what's the time" in query:
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir!, The Time is {strftime}")

        elif 'open chrome' in query:
            speak('Ok Sir!')
            webbrowser.open("Chrome")

        elif 'close the chrome' in query:
            speak("Closing Chrome")
            os.system("TASKKILL /f /IM Chrome.exe")      

        elif 'youtube' in query:
            speak('ok Sir!')
            url = "http:\\youtube.in"
            webbrowser.open_new_tab(url)

        elif 'amazon' in query:
            speak('Yes Sir!')
            webbrowser.open_new_tab(url="http:\\amazon.in")

        elif 'news' in query:
            webbrowser.open_new_tab(
                "https:\\timesofindia.indiatimes.com\home\headlines")
            speak("Here are some Headlines from the Times of India.")
            #time.sleep(3)

        #elif 'search' in query:
            #query = query.replace("search", "")
            #speak('OK Sir!')
            #webbrowser.open_new_tab(query)
            #time.sleep(3)

        elif "search" in query:
           speak("Ok what you want to search")
           query= record()
           #driver=webdriver.Chrome("C:\\Users\\Rohan\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
           driver=webdriver.Chrome("C:\\Users\\Rohan\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
           driver.get("http:\\google.co.in")
           searchbox=driver.find_element_by_name('q')
           searchbox.send_keys(query.split(" "))
           searchbox.submit()
                 
        elif 'wikipedia' in query:
            try:
               speak('Searching Wikipedia...')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query,sentences=2)
               speak('According to Wikipedia:{}\n'.format(results))

            except Exception as e:
                speak("Sorry Sir!, I cannot find information on wikipedia...")

        elif 'open code' in query:
            speak('Ok Sir!')
            codepath = "C:\\Users\Rohan\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'close the code' in query:
            speak("Closing Code")
            os.system("TASKKILL /f /IM Code.exe")    

        elif 'open note' in query:
            speak('Sure Sir!')
            code_path=('C:\Windows\System32\\notepad.exe')
            os.startfile(f'{code_path}') 

        elif 'close the note' in query:
            speak("Closing Notepad")
            os.system("TASKKILL /f /IM notepad.exe")   

        elif 'write' in query or 'create' in query:
            speak("OK Sir!, what you want to write in a File.")
            outfile=open('file.txt','w')
            query=record()
            print(query,file=outfile)
            outfile.close()
            speak("\nSir!,can i read for you..")
            query=record()
            try:
               if "yes" in query:
                  outfile=open('file.txt','r')
                  for line in outfile:
                    speak(line)
                  outfile.close()

               elif "no" in query: 
                  speak("Alright Sir!")

            except Exception:
                speak('Sorry Sir!, I cannot read the file')                          

        elif 'who are you' in query or 'about yourself' in query:
            speak("i'm Friday. Speed AMD Ryzen 5 3500x, 6 Core Processor 3.6 Gigahertz Overclock Speed upto 4 Gigahertz. Memory 16 Gigabytes XPG AData with RGB.")

        elif 'made you' in query:
            speak('I was Created by Rohan.')

        elif 'log off' in query or 'sign out' in query:
            speak(
                "OK Sir!, Your pc will log off in 10 second make sure you exit from all Application")
            subprocess.call(["shutdown", "/l"])
            time.sleep(3)

        elif 'power off' in query or 'shut down' in query:
            speak('OK Sir!,Shutting Down the Computer.Have a Good day Sir!')
            subprocess.call(["shutdown", "/sg"])
            time.sleep(4)

        elif 'restart' in query:
            speak('OK Sir!,Restarting the Computer.')
            subprocess.call(["shutdown", "/g"])
            time.sleep(4)

        elif 'sleep' in query:
            speak("ok Sir!, i can Sleep now you can call me any Time")
            break

        elif "you there" in query or 'there friday' in query:
            choices=random.choice(["i'm here sir!","Yes Sir!"])
            speak(f'{choices}')
        
        elif 'hello' in query:
            choices=random.choice(["Hello Sir!","Hello Sir! How are you"])
            speak(f"{choices}")

        elif "i am fine" in query or "i'm fine" in query:
            speak("It's Good you are fine Sir!")

        elif "how are you" in query or "how about you" in query:
            speak("i'm fine sir!, Thank you for asking me.")

        elif 'what are you doing' in query:
            choices = random.choice(["Nothing Sir! you Say.", "i'm just Performing some Task. what about you"])
            speak(f"{choices}")   

        elif "my birthday date" in query:
            date = ('23/10 october/1997')
            speak(f"Ofcourse Sir!, Your Birthday Date is {date}")

        elif "your birthday date" in query:
            speak("i don't know Sir!, i have no Birthday date. I was created by Mr.Rohan. Maybe he know's")

        elif 'can you perform some task for me' in query or 'can you perform some task' in query:
            speak('Yes Sir!, Just say and i do for You')


if __name__ == '__main__':
    while True:
        query = record()
        # taskExecution(query)
        Permission = query
        if 'hello' in Permission:
            lst1 = random.choice(["i'm always here for you Sir!",
                              "it's good to see you Sir!",'Yes Sir! How can i help you.'])
            speak(f"{lst1}")
            taskExecution(query)    

        elif 'exit' in Permission:
            speak("OK Sir!, Thank's for Using Me. Have a Good day")
            sys.exit()