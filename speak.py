import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 125)  
engine.setProperty("volume", 1)  

engine.say("Hello!,Welcome, I am a text-to-speech engine, type what you want to speak with me.")

engine.runAndWait()
print("Enter something...")
while True:
    inputuser = input("Enter: ")
    if inputuser == "!close":
        break
    engine.say(inputuser)
    engine.runAndWait()
engine.say("Thanks for use me!")
print("Bye-Bye,Have a nice Day...")
engine.runAndWait()