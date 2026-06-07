import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    print(c)
    
if(__name__=="__main__"):
    speak("Initializing jarvis.....")
    
while True:
    r = sr.Recognizer()
    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("listioning....")
            audio = r.listen(source, timeout=2 , phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "Ajay"):
            speak("Yess Boss")
            with sr.Microphone() as source:
                print(" Jarvis active....")
                audio = r.listen(source)
                command  = r.recognize_google(audio)
                
                processCommand(command)
    except Exception as e:
        print("error ;{0}".format(e))