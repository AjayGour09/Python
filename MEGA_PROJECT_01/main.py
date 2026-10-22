
import os
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

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# =========================
# SPEECH ENGINE
# =========================

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()


def speak(text):
    try:
        text = str(text)
        print("Jarvis:", text)

        engine.say("Ajay")
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Speak Error:", e)


# =========================
# OPENAI AI PROCESSING
# =========================

def aiProcess(command):
    try:
        if not OPENAI_API_KEY:
            return (
                "OpenAI API key is not configured. "
                "Please set the OPENAI_API_KEY environment variable."
            )

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful AI voice assistant. "
                        "Give clear, concise and useful answers."
                    )
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return (
            response.choices[0].message.content
            or "Sorry, I could not generate a response."
        )

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry Sir, I could not process your request."


# =========================
# NEWS PROCESSING
# =========================

def fetchNews():
    if not NEWS_API_KEY:
        speak("News API key is not configured.")
        return

    speak("Fetching latest news.")

    try:
        url = "https://newsapi.org/v2/top-headlines"

        response = requests.get(
            url,
            params={
                "country": "us",
                "apiKey": NEWS_API_KEY
            },
            timeout=10
        )

        if response.status_code != 200:
            print("News API Error:", response.text)
            speak("Unable to fetch news.")
            return

        data = response.json()
        articles = data.get("articles", [])

        if not articles:
            speak("No news found.")
            return

        for article in articles[:5]:
            title = article.get("title")

            if title:
                print(title)
                speak(title)

    except requests.RequestException as e:
        print("News Request Error:", e)
        speak("News service is unavailable.")

    except Exception as e:
        print("News Error:", e)
        speak("An error occurred while fetching news.")


# =========================
# COMMAND PROCESSOR
# =========================

def processCommand(command):
    command = command.lower().strip()

    if not command:
        return

    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")

    elif "news" in command:
        fetchNews()

    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            try:
                speak(f"Playing {song}.")
                pywhatkit.playonyt(song)

            except Exception as e:
                print("Music Error:", e)
                speak("Unable to play the song.")

        else:
            speak("Please tell me the song name.")

    else:
        speak("Thinking.")

        output = aiProcess(command)

        print(output)
        speak(output)


# =========================
# MAIN PROGRAM
# =========================

def main():
    speak("Initializing Jarvis. Hello Ajay Sir.")

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening for wake word...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("Yes Sir.")

                with sr.Microphone() as source:
                    print("Jarvis Active. Listening for command...")

                    recognizer.adjust_for_ambient_noise(
                        source,
                        duration=0.5
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
            print("Listening timeout. Waiting again...")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print("Speech Recognition Error:", e)
            speak("Speech recognition service is unavailable.")

        except KeyboardInterrupt:
            print("\nJarvis stopped.")
            speak("Goodbye Ajay Sir.")
            break

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
