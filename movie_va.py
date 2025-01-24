import imdb
import pyttsx3
import speech_recognition as sr


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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        speak("Listening")
        audio = r.listen(source)
        said = ""
    
    try:
        said = r.recognize_google(audio)
        print(said)
    
    except:
        speak("Didn't get that")
    
    return said.lower()





def get_movie(text):
    moviesdb = imdb.IMDb()
    movies = moviesdb.search_movie(text)

    speak("Searching for " + text)

    if (movies):
        
        
        #for movie in movies:
        movie = moviesdb.get_movie(movies[0].movieID)
        
        speak("Found this ")
        speak(f"{movie['title']}, {movie['year']}, Starring: {movie['cast'][0]}, and {movie['cast'][1]}")

    else:
        speak("No result found")


def actor_intersection(name1, name2):
    moviesdb = imdb.IMDb()
    actor1 = moviesdb.get_person(moviesdb.search_person(name1)[0].personID)
    actor2 = moviesdb.get_person(moviesdb.search_person(name2)[0].personID)

    print(actor1['name'])
    print(actor1['data']['filmography'])
    
    # for movie in actor1['filmography']['actor']:
    #     print(movie['title'])










speak("Pick a movie")
get_movie(get_audio())
#get_movie('La La Land')
#actor_intersection("Ryan Gosling", "Emma Stone")

    
