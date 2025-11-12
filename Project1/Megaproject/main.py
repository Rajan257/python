# # import speech_recognition as sr
# # import webbrowser
# # import pyttsx3
# # import musicLibrary
# # import requests
# # # pip install pocketsphinx

# # recognizer = sr.Recognizer()
# # engine= pyttsx3.init()
# # newsapi = "9a2944e78f4040139e15df50d245f596"
# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()


# # def processCommand(c):
# #     if "open google" in c.lower():
# #           webbrowser.open("https://google.com")

# #     elif "open facebook" in c.lower():
# #           webbrowser.open("https://facebook.com")
        
# #     elif "open youtube" in c.lower():
# #           webbrowser.open("https://youtube.com")

# #     elif "open linkedin" in c.lower():
# #           webbrowser.open("https://linkedin.com")

# #     elif c.lower().startswith("play"):
# #           song =c.lower().split(" ")[1]
# #           link= musicLibrary.music[song]
# #           webbrowser.open(link)

# #     elif "news" in c.lower():
# #           r = requests.get("https://newsapi.org/v2/top-headlines/sources?apiKey={newsapi}")
          
# #           if r.status_code == 200:
# #              data = r.json()
# #              #extract the articles
# #              articles = data.get("articles", [])


# #              #speak Top Headlines:
# #              for  article in articles:
# #               speak(article['title'])
          
# #     else:
# #         #let Open AI handle the request
# #               pass

# # if __name__=="__main__":
# #     speak("Initializing jarvis....")
# #     while True:
# #       #listen for the fake words "jarvis"
# #     #obtain audio from microphone
    
# #         r = sr.Recognizer()
          

# #         print("Recognizing....")
# #         try:
               
# #             with sr.Microphone() as source:
# #                 print("Listening...!")

# #                 audio = r.listen(source,timeout=2,phrase_time_limit=1)
          
# #             word=r.recognize_google(audio)
# #             if(word.lower()=="jarvis"):
# #                 speak("how can i help you")
# #                     #listen for command
# #                 with sr.Microphone() as source:
                       
# #                     print("Sonia active...!")

# #                     audio = r.listen(source)
# #                     command=r.recognize_google(audio)

# #                     processCommand(command)
             
    

# #         except Exception as e:
# #             print("Error; {0}".format(e))     




# # #open ai ?


# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# # pip install pocketsphinx

# recognizer = sr.Recognizer()
# engine = pyttsx3.init() 
# newsapi = "9a2944e78f4040139e15df50d245f596"

# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

# def aiProcess(command):
#     client = OpenAI(api_key="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",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#         if r.status_code == 200:
#             # Parse the JSON response
#             data = r.json()
            
#             # Extract the articles
#             articles = data.get('articles', [])
            
#             # Print the headlines
#             for article in articles:
#                 speak(article['title'])

#     else:
#         # Let OpenAI handle the request
#         output = aiProcess(c)
#         speak(output) 





# if __name__ == "__main__":
#     speak("Initializing Sonia....")
#     while True:
#         # Listen for the wake word "Sonia"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
         
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                 speak("Ya")
#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Sonia Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)


#         except Exception as e:
#             print("Error; {0}".format(e))









# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import requests
# from gtts import gTTS
# import pygame
# import os

# # Replace with your actual NewsAPI key
# newsapi = "9a2944e78f4040139e15df50d245f596"

# # Speak using gTTS + pygame
# def speak(text):
#     tts = gTTS(text)
#     tts.save("temp.mp3")
#     pygame.mixer.init()
#     pygame.mixer.music.load("temp.mp3")
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

# # Handle commands
# def processCommand(command):
#     command = command.lower()

#     if "open google" in command:
#         webbrowser.open("https://google.com")
#         speak("Opening Google")

#     elif "open youtube" in command:
#         webbrowser.open("https://youtube.com")
#         speak("Opening YouTube")

#     elif "open facebook" in command:
#         webbrowser.open("https://facebook.com")
#         speak("Opening Facebook")

#     elif "open linkedin" in command:
#         webbrowser.open("https://linkedin.com")
#         speak("Opening LinkedIn")

#     elif "news" in command:
#         try:
#             r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#             if r.status_code == 200:
#                 data = r.json()
#                 articles = data.get('articles', [])
#                 speak("Here are the top 5 news headlines.")
#                 for article in articles[:5]:
#                     speak(article['title'])
#             else:
#                 speak("Unable to fetch news at the moment.")
#         except Exception as e:
#             print("News error:", e)
#             speak("An error occurred while getting news.")
    
#     else:
#         speak("Sorry, I didn't understand that command.")

# # Main loop
# if __name__ == "__main__":
#     speak("Initializing Sonia...")

#     while True:
#         try:
#             recognizer = sr.Recognizer()
#             with sr.Microphone() as source:
#                 print("Say 'Sonia' to activate...")
#                 audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
#             wake_word = recognizer.recognize_google(audio)

#             if wake_word.lower() == "jarvis":
#                 speak("Yes, how can I help you?")
#                 with sr.Microphone() as source:
#                     print("Listening for command...")
#                     audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#                 command = recognizer.recognize_google(audio)
#                 print("You said:", command)
#                 processCommand(command)

#         except sr.UnknownValueError:
#             print("Could not understand audio.")
#         except sr.RequestError as e:
#             print(f"Speech recognition error: {e}")
#         except Exception as e:
#             print(f"Other error: {e}")

























import speech_recognition as sr
import webbrowser
import requests
from gtts import gTTS
import pygame
import os
import musicLibrary  # your custom music dictionary

# Replace with your actual NewsAPI key
newsapi = "9a2944e78f4040139e15df50d245f596"

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif command.startswith("play"):
        song_name = command.replace("play", "").strip()
        if song_name in musicLibrary.music:
            link = musicLibrary.music[song_name]
            speak(f"Playing {song_name}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song_name} in your music library.")

    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                speak("Here are the top 5 news headlines.")
                for article in articles[:5]:
                    speak(article['title'])
            else:
                speak("Unable to fetch news at the moment.")
        except Exception as e:
            print("News error:", e)
            speak("An error occurred while getting news.")
    
    else:
        speak("Sorry, I didn't understand that command.")

# Main Loop
if __name__ == "__main__":
    speak("Initializing Sonia...")

    while True:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say 'Sonia' to activate...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print("You said:", command)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
        except Exception as e:
            print(f"Other error: {e}")




