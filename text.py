import pyttsx3
text = pyttsx3.init()
enter = input("enter the text that you want to listen: ")
text.say(enter)
text.runAndWait()
