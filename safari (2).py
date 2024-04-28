import subprocess
import requests
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import webbrowser
import time
import requests
import shutil
import pyautogui

from playsound import playsound
from twilio.rest import Client
from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
playsound("power up.mp3")  
#playsound.playsound("safari.mp3")	
def wishMe():
    	
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("safari")
	speak("I am your Assistant")
	speak(assname)
	speak("I am here to assist you in all your tasks")
	

def usrname():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome ")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome ", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 0.5
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	usrname()
	
	while True:
		
		query = takeCommand().lower()
		
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
   
		
   
		elif 'turn on light' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=3&value=0")
			speak('lights are turned on')

		elif 'turn off light' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=3&value=1")
			speak('lights are turned off')
   
		elif 'turn on fan' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=2&value=0")
			speak('fan is turned on')
   
		elif 'turn off fan' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=2&value=1")
			speak('fan is turned off')
   
		elif 'open the curtains' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=1&value=0")
			speak('curtains are opened')
   
		elif 'close the curtains' in query:
			val=requests.get("https://blynk.cloud/external/api/update?token=I9Q36o6gWxr2GmRxCryMRx5Cx4AeaAmU&dataStreamId=1&value=1")
			speak('curtains are closed')

		elif 'open youtube' in query or "youtube" in query:
			speak(" Youtube is on your screen sir\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query or "Google" in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")
   
		elif 'song please' in query or 'play some songs' in query or 'could you play some song' in query:
			speak('sir what song should i play')
			song=takeCommand()
			webbrowser.open(f'https://open.spotify.com/search/{song}')
			time.sleep(8)
			pyautogui.moveTo(x=980,y=537)
			pyautogui.click(x=980,y=537)
			time.sleep(4)
			pyautogui.click(x=1768,y=25)
			speak('playing'+song)
   
		elif 'play' in query or 'can you play' in query or 'please play' in query:
			speak('Here you go')
			query=query.replace("play","")
			query=query.replace("can you play","")
			query=query.replace("please play","")
			webbrowser.open(f'https://open.spotify.com/search/{query}')
			time.sleep(8)
			pyautogui.moveTo(x=980,y=537)
			pyautogui.click(x=980,y=537)
			time.sleep(4)
			pyautogui.click(x=1768,y=25)
			speak('playing'+query)
			print('playing'+query)
			

		elif 'safari stop' in query or 'safari play' in query or 'safari pause' in query or 'pause' in query:
			pyautogui.press('playpause')
   
		elif 'safari next song' in query:
			pyautogui.press('nexttrack')
   
		elif 'safari volume up' in query:
			pyautogui.press('volumeup')
   
		elif 'safari volume down' in query:
			pyautogui.press('volumedown')
  
		elif 'what`s the time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S")
			speak(f"Sir, the time is {strTime}")

		elif 'open chrome' in query or "chrom" in query:
			codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
			os.startfile(codePath)

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "what is your name" in query:
			speak("i am safari")

		elif 'safari now you can stop' in query:
			speak("Thanks for giving me your time")
			exit()

		elif 'safari' in query:
			speak('what can i do for you sir')
	
		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Group Number 11, the members are akshay rathod, ishita patil, omkar apre and omkar rokade")

			
		elif 'tell us joke' in query or "tell us a joke" in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definately your human.")

		elif "why have you came to this world" in query:
			speak("Thanks to Group Number 11. further It's confidential")


		elif 'open power point presentation' in query:
			speak("opening Power Point presentation")

		elif 'what is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Group Number 11")

		elif 'who created you' in query:
			speak("I was created by Akshay Rathod, Omkar Apre, Ishita Patil and Omkar Rokade ")

		

		elif 'news' in query:
			
			try:
				jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call(["shutdown", "/s"])
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop safari from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "locate me safari" in query or "locate me" in query:
			query = query.replace("where is", "")
			location = query
			webbrowser.open("https://earth.google.com/web/")
            
			speak("connecting to the satelite and sending information to the server securing connection.here you are sir")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('safari.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("safari.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									
                     expected_size =(total_length / 1024) + 1):
					if ch:
					    Pypdf.write(ch)
				
		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")
        
		elif "who are the members of group number 11" in query:
    			speak("member of group number 11 are Akshay Rathod, Omkar Apre, Ishita Patil and Omkar Rokade")
        
		elif "who is the guide of group number 11" in query:
    			speak("guide of group 11 is Professor Shikha Sharma Mam")
	    
		elif "safari tell us about yourself" in query:
    			speak("OK i am safari created by members of group number 11 .i am virtual assistant.who can help you in your day today life.i can do virtually whatever you want.such as webbrowsing,opning applications,writing short notes.i can be your 24 7 assistant to help you sir.")


		# elif "" in query:
			# Command go here
			# For adding more commands
