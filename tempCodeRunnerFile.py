try:
    import pyttsx3 as tts
except ModuleNotFoundError:
    tts = None

class Shoutout:
    def __init__(self):
        self.names = []
        for i in range(5):
            name = input("Enter your name: ")
            self.names.append(name)

# Object banakar input c