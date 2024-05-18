import pyttsx3

engine = pyttsx3.init()

while True:
    text = input("Enter What You Want To Speak:")
    if text == "exit":
        break
    engine.say(text)
    engine.runAndWait()











