import datetime
import webbrowser
import pyttsx4
import speech_recognition as sr


def take_commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")

            # for listening the command in indian english
            audio = r.recognize_google(audio, language='en-in')
            webbrowser.open(audio)
            # for printing the query or the command that we give
            print("the query is printed='", audio, "'")
        except Exception as e:
            print(e)
            return "None"

    return audio


def Speak(audio):

    # initial constructor of pyttsx3
    engine = pyttsx4.init()

    # getter and setter method
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)


# Driver Code
if __name__ == '__main__':
    command = take_commands()

    if "day" in command:
        tellDay()
