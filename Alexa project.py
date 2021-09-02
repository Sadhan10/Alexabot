import speech_recognition as sr
import pyttsx3
import pywhatkit
engine=pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)
engine.say("I am alexa")
listener=sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command =command.lower()
            if 'alexa' in command:
                speak(command)
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        speak("playing"+song)
        pywhatkit.playonyt(song)
        print(song)
    run_alexa()

