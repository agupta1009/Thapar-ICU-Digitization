import speech_recognition as sr

r = sr.Recognizer()

def try1():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Recording started ")
        voice = r.listen(source)

        try:
            text = r.recognize_wit(voice)
            print(text)
        except:
            print("NAHHH YOU SHIT")

try1()