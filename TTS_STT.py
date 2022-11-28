# Speech To Text — Python
# pip install SpeechRecognition
# Download PyAudio from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl and
# NOT pip install PyAudio (Works only in Linux)

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something and pause, no need to press any key")
    audio = r.listen(source)
    print("Got you")
try:
    WhatUSpoke = r.recognize_google(audio, language="")
    print("Language: English")
    print("What you spoke:", WhatUSpoke)
    
except:
    pass
