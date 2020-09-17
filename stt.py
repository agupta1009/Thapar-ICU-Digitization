import pyttsx3 as p
import speech_recognition as sr
from utils import recognize_speech_from_mic
engine=p.init()
engine.setProperty('rate',200)
engine.setProperty('volume',1.0)
# will pick the keys from the data base
record={
    "patient Name":[],
    "patient ID": [],
    "patient Age":[],
    "doctor handling the case":[],
    "symptoms":[],
    "medicine":[],
}
r = sr.Recognizer()
m = sr.Microphone()
for keys in record:
    # computer will speak to give the output
    p.speak(f" please tell the {keys}")
    print(f" please tell the {keys}")
    # transcription received
    text=recognize_speech_from_mic(r, m)
    print(text)
    record[keys].append(text)

# here the records are printed can be directly saved to database
for keys in record:
     print(f"{keys} : {record[keys]}")
    
