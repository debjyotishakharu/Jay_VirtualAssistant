from Tasks import *
from general_conv import *

from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def main():
    greet_user()
    while True:
        user_command = listen()
        if "task" in user_command:
            speak("what is the command sir?")
            user_command = listen()
            if "play" in user_command:
                play_youtube(user_command)   
            elif "youtube" in user_command:
                youtube_search(user_command)
            elif "exit" in user_command:
                speak("Okay, Finally I can have some rest!!!")
                break
            elif "search" in user_command:
                chrome_search(user_command)
            elif "camera" in user_command:
                open_camera()
            elif "cmd" in user_command:
                open_cmd()
            elif "calculator" in user_command:
                open_calculator()
            else:
                speak("Sorry did not understand what you just said. Try again")

        elif "exit" in user_command:
            speak("goodbye")
            break

        else:
            response=dialogpt_conv(user_command)
            print(response)
            speak(response)
            

if __name__ == "__main__":
    main()
