import pyttsx3

class Shoutout:
    def __init__(self):
        self.names = ["Navneet","saurabh","yash","yogita","rachi"]

obj = Shoutout()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak each name immediately
for i in obj.names:
    print("Speaking:", i)   # Debugging line
    engine.say(f"Hello {i}, congrats for completing the exercise!")
engine.runAndWait()   # <-- run after each say
