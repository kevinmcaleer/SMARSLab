import pyaudio
import wave
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()
m = sr.Microphone()

print("Listening")
with m as source: r.adjust_for_ambient_noise(source)

while True:
    print("Say Something")
    with m as source: audio = r.listen(source)
    print("Got it")

    try:
       phrase = r.recognize_google(audio)
       if phrase == "robot":
           engine.say("Im listening")
           engine.runAndWait()
           with m as source: audio = r.listen(source)
           phase = r.recognize_google(audio)
        
           print("you said" + r.recognize_google(audio))
           engine.say("You said " + r.recognize_google(audio))
           engine.runAndWait()
    except LookupError:
        print("Could not understand audio")

RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2

RESPEAKER_INDEX = 1
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'output.wav'

p = pyaudio.PyAudio()

stream = p.open(
            rate = RESPEAKER_RATE,
            format = p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input = True,
            input_device_index=RESPEAKER_INDEX,)

print("* recording")
engine.say("Recording")
engine.runAndWait()

frames = []

for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(RESPEAKER_CHANNELS)
wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
wf.setframerate(RESPEAKER_RATE)
wf.writeframes(b''.join(frames))
wf.close()


