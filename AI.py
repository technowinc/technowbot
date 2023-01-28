import clipboard
import datetime
import os
import psutil
import pyautogui
import pyjokes
import pyttsx3
import wikipedia
import pywhatkit
import wolframalpha
import smtplib
import ctypes
from urllib.request import urlopen
import requests
import tkinter
import subprocess
import json
import smtplib
import speech_recognition as sr
import time as ti
import webbrowser as we
from email.message import EmailMessage
from newsapi import NewsApiClient
from time import sleep

user = "Arnav"
assistant = "Technow"
engine = pyttsx3.init()
voices = engine.getProperty("voices")


#engine.setProperty("voice", voices[0].id)
# Note: rmeove note on below command for initiating fmeale voice
engine.setProperty("voice", voices[0].id)
def output(audio):
    print(audio) # For printing out the output
    engine.say(audio)
    engine.runAndWait()

# For getting the device index you can execute this code So if you want to change the device you can do that.
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
#         index, name))

def inputCommand():
    query = input() # For getting input from CLI
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 0
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            output("Speak again, Sauron")
    return query
def greet():
        hour = datetime.datetime.now().hour
        if (hour >= 6) and (hour < 12):
           output(f"Good Morning {user}, this is Technow")
        elif (hour >= 12) and (hour < 18):
           output(f"Good afternoon {user}, this is Technow")
        elif (hour >= 18) and (hour < 21):
           output(f"Good Evening {user}, this is Technow")
           output("How may I assist you, Chairman and Founder?")
def sendEmail():
    senderemail = "arnavnandurkar@mksssvision.edu.in"
    password = "technowinc"
    email_list = {
        "one": "gopalnandurkar@gmail.com", # Temporary Email
        "two": "kalyaninandurkar@gmail.com"
    }
    try:
        email = EmailMessage()
        output("To which Death Eater do you want to send the mail?")
        name = inputCommand().lower()
        email['To'] = email_list[name]
        output("What is the subject of the mail?")
        email["Subject"] = inputCommand()
        email['From'] = senderemail
        output("What should I Say?")
        email.set_content(inputCommand())
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(senderemail, password)
        s.send_message(email)
        s.close()
        output("Email has been sent")
    except Exception as e:
        print(e)
        output("Unable to send the Email")
def sendWhatMsg():
    user_name = {
        'Kalyani Nandurkar': '+91 9325459875'
    }
    try:
        output("To whom you want to send the message, Chairman of technow?")
        name = inputCommand()
        output("What is the message?")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+inputCommand())
        sleep(3)
        pyautogui.press('enter')
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")
def weather():
    city = "Pune"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    output("What news do thou seek, master?")
    topic = inputCommand()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        output(y["description"])
def idea():
    output("What's your new idea or invention?")
    data = inputCommand().title()
    output("Your latest idea or invention was: " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)
greet()
# Then with while true we can make it a infinite loop on command
while True:
    # Getting input from the user
    query = inputCommand().lower()
    # According to the query if query have respective word we will execute the respective command
    if ("time" in query):
        output("Current time is " +
               datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in query):
        output("Current date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))

    elif ('send mail' in query):
        sendEmail()

    elif ('message' in query):  
        print("Sending...")
        sendWhatMsg()

    elif ("search" in query):
        output("what you want to search?")
        we.open("https://www.google.com/search?q="+inputCommand())

    elif ("youtube" in query):
        output("What you want to search on Youtube?")
        pywhatkit.playonyt(inputCommand())

    elif ('weather' in query):
        weather()

    elif ("news" in query):
        news()

    elif ("read" in query):
        output(clipboard.paste())

    elif ("covid" in query):
        r = requests.get(
            'https://coronavirus-19-api.herokuapp.com/all').json()
        output(
            f'Confirmed Cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}')

    elif ("workspace" in query):
        output("Which workspace you want to work on")
        os.startfile("D:\\Work Spaces\\" +
                     inputCommand()+".code-workspace")

    elif ("joke" in query):
        output(pyjokes.get_joke())

    elif ("idea" in query):
        idea()

    elif ("do you know" in query):
        ideas = open("data.txt", "r")
        output(f"One of your inventions was:\n{ideas.read()}")

    elif ("screenshot" in query):
        pyautogui.screenshot(str(ti.time()) + ".png").show()

    elif "cpu" in query:
        output(f"Cpu is at {str(psutil.cpu_percent())}")

    elif "who" in query:
        output("I am Technow, the voice assistant running on Artificial Intelligence created by Arnav Nandurkar. What may I do for you?")
    
    elif "founding" in query:
        output("Technow Tehcnologies Incorporated was started as The Science Club on 30 March 2016, adn on 30 March 2023 it will celebrate it's 7th anniversary. It was founded by my creator, who is the Chairman and CEO. The Director is Sarvesh Sonawne.")

    elif "hello" in query:
        greet()
    
    elif "good night" in query:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            output(f"Good Night {user}! Tomorrow you have to go to Vision English Medium School!")
        else:
            output(f"Good Night {user}! Tomorrow you have to go to Vision English Medium School!")
        quit()
    elif "bye" in query:
        output('The Technow AI Assistant is closing. Technow Technologies Incorporated wishes you a pleasant day! ')
    
    elif "question" in query:
            output('Ask me anything related to geography')
            question=inputCommand()
            app_id="3YX6X9-E6UX6W34TW"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            output(answer)
            
    elif "China" in query:
        output("DOWN WITH CHINA!")
    
    
    elif 'how are you' in query:
        output("I'm always fine. I'm artificial intelligence running on a computer. Of course I would be fine." or "Good, thank you, and you?")

    elif 'fine' in query:
        output("Fine? Good? Not for long.")
 
 