import pyttsx3

engine = pyttsx3.init(driverName='espeak')
b = int(input("type in the speed normall is 125: "))
engine.setProperty('rate', b) 

while True:
    a = input(": ")
    engine.say(a)
    engine.runAndWait()
    if a == "exit":
        exit()
