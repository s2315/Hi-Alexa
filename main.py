import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()    # Receive commands
engine = pyttsx3.init()       # For talking
voices = engine.getProperty('voices')  # For female voice
engine.setProperty('voice', voices[1].id)  #Setting the female voice from second index,i.e [1]

def talk(text):        # Whatever I will say alex with repeat that
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Hi I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'selin' in command:
                command = command.replace('selin', '')
                print(command)
    except:
        pass
    return command


def run_Alexa():
    command = take_command()
    print(command)
    if 'play' in command: # if I use word play in my sentence
        song = command.replace('play', '') # replacing play while alexa is replaying
        talk('playing your song' + song)
        pywhatkit.playonyt(song) # playing song on youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') # Telling the current time
        talk('Now the time is  ' + time)
    elif 'who is the' in command: # searching on wikipedia
        person = command.replace('who is the ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is history' in command: # searching history on wikipedia
        place = command.replace('what is the history', '')
        info = wikipedia.summary(place, 1)
        print(info)
        talk(info)
    if 'on youtube' in command: # if I use word play in my sentence
        info = command.replace('on youtube', '') # replacing play while alexa is replaying
        talk('searching....' + info)
        pywhatkit.playonyt(song)
    else:
        talk('Please say the command again.')


while True:
    run_Alexa()

