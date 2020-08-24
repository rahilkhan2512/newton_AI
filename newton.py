
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	name = "rahil"
	speak("hii sir, i am newton an AI that is an artificial intelligence software")
	hour = int(datetime.datetime.now().hour)
	if (hour >= 0 and hour <12):
		speak(f"Good Morning {name}!")
	elif (hour >=12 and hour < 18):
		speak(f"Good Afternoon {name}!")
	else:	
		speak(f"Good Evening {name}!")
	speak("I am newton an AI , Please tell me how i can help you?")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print("Say again please...")
		return "None"
	return query

if __name__ == "__main__":
	wishme()
	password="be positive"
	speak("Please say password to begin!")
	pswd = takeCommand().lower()
	count=5
	while True:

		if pswd == password:
    		
			query = takeCommand().lower()

			if 'wikipedia' in query:
				speak('Searching Wikipedia...')
				query = query.replace("wikipedia","")
				results = wikipedia.summary(query,sentences=2)
				speak('According to wikipedia...')
				print(results) 
				speak(results)
				

			elif 'open youtube' in query:	
				webbrowser.open("https://www.youtube.com")
			
			
			elif 'open google' in query:	
				webbrowser.open("https://www.google.com")

			elif 'open whatsapp' in query:	
				webbrowser.open("https://web.whatsapp.com/")
			
			elif 'play music' in query:
				music_dir = "D:\RAHIL\Music"
				songs = os.listdir(music_dir)
				print(songs)
				os.startfile(os.path.join(music_dir,songs[0]))
			
			elif 'the time' in query:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				speak(f" rahil the time is {strTime}")
			
			elif 'open code' in query:
				codePath = "C:\\Users\\ADNMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
				os.startfile(codePath)

			
			
			elif ('quit' or 'close') in query:
				speak("Ok Sir i m quitting!")
				print("Quitting...")
				break
		else:
			if count ==0:
				speak("Nonaudible")
				speak("You have exceed the permissible limit please try again!")
				speak("I am quitting!")
				break
			else:	
				count =count -1
				print(f"{count} attemp is remaining...")
				speak("Please say your password!")
				pswd = takeCommand().lower()