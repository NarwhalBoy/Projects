import imdb
import pyttsx3
import speech_recognition as sr
import datetime

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')

    engine.setProperty('rate', rate-20)

    engine.say(text)
    engine.runAndWait()





def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshhold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
    
    try:
        said = r.recognize_google(audio)
        print(said)
    
    except:
        speak("Didn't get that")
    
    return said.lower()


speak("Say the First Movie Name")
first = get_audio()
speak("Say the Second Movie Name")
second = get_audio()

print("First movie is", first, "and second movie is", second)

# def get_movies():

    