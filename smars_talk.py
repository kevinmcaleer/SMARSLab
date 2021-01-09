import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

if mic.wakeup('quad'):
    print('wake up')
    data = mic.listen()
    text = mic.recognize(data)
    if text:
        time.sleep(1)
        print('Recognized %s' % text)
