import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pywhatkit
from openai import OpenAI

# =========================
# CONFIGURATION
# =========================

NEWS_API_KEY = "5-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# =========================
# SPEECH ENGINE
# =========================

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Male voice
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()


def speak(text):
    try:
        print("Jarvis:", text)
        engine.say("Ajay")
        engine.say(str(text))
        engine.runAndWait()
    except Exception as e:
        print("Speak Error:", e)


# =========================
# OPENAI
# =========================

def aiProcess(command):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI Error: {e}"


# =========================
# COMMAND PROCESSOR
# =========================

def processCommand(command):

    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif command.startswith("play"):
        

        try:
            
        
           song = command.replace("play", "").strip()
           if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
           else:
            speak("Please tell a song name")
        except Exception as e:
            print("Music Error:", e)
            speak("Unable to play song")

    elif "news" in command:

        speak("Fetching latest news")

        try:
            url = (
                f"https://newsapi.org/v2/top-headlines"
                f"?country=us&apiKey={NEWS_API_KEY}"
            )

            r = requests.get(url)

            if r.status_code == 200:

                data = r.json()
                articles = data.get("articles", [])

                if not articles:
                    speak("No news found")
                    return

                for article in articles[:5]:
                    title = article["title"]
                    print(title)
                    speak(title)

            else:
                print(r.text)
                speak("Unable to fetch news")

        except Exception as e:
            print(e)
            speak("News service error")

    else:

        speak("Thinking")

        output = aiProcess(command)

        print(output)

        speak(output)


# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        try:

            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening for wake word...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            print("Heard:", word)

            if "jarvis" in word.lower():

                speak("Yes Sir")

                with sr.Microphone() as source:

                    print("Jarvis Active...")

                    recognizer.adjust_for_ambient_noise(
                        source,
                        duration=1
                    )

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=8
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timeout")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except Exception as e:
            print("Error:", e)