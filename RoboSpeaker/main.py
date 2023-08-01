import win32com.client as wincom


if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to RoboSpeaker 1.1 Created by Manjusha")
    while True:
        x = input("Enter what you want me to speak ")
        if x == "quit" or 'q':
            speak.Speak("Bye bye friends")
            break
        speak.Speak(x)