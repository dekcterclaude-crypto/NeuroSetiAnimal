import tkinter as tk
import threading
import sounddevice as sd
import soundfile as sf
import simpleaudio as sa
import speech_recognition as sr

FILENAME = "record.wav"
recording = False
recognizer = sr.Recognizer()
audio_data = []



def start_recording():
    global recording, audio_data
    audio_data = []
    recording = True

    def record():
        with sd.InputStream(samplerate=44100, channels=1, callback=callback):
            while recording:
                sd.sleep(100)

    threading.Thread(target=record).start()


def callback(indata, frames, time, status):
    if recording:
        audio_data.append(indata.copy())



def stop_recording():
    global recording
    recording = False

    if audio_data:
        data = b"".join([chunk.tobytes() for chunk in audio_data])
        sf.write(FILENAME, b"".join([chunk.tobytes() for chunk in audio_data]), 44100, format='WAV')
        print("Запись сохранена:", FILENAME)


def play_audio():
    wave_obj = sa.WaveObject.from_wave_file(FILENAME)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def recognize_speech():
    try:
        with sr.AudioFile(FILENAME) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru-RU")
        result_label.config(text="Распознанный текст:\n" + text)
    except:
        result_label.config(text="Ошибка распознавания.")


root = tk.Tk()
root.title("Диктофон (Python 3.14)")
root.geometry("400x350")

title = tk.Label(root, text="🎤 Диктофон", font=("Arial", 20))
title.pack(pady=10)

btn_record = tk.Button(root, text="Начать запись", font=("Arial", 14),
                       command=start_recording, bg="red", fg="white")
btn_record.pack(pady=5)

btn_stop = tk.Button(root, text="Остановить запись", font=("Arial", 14),
                     command=stop_recording, bg="gray", fg="white")
btn_stop.pack(pady=5)

btn_play = tk.Button(root, text="▶ Воспроизвести", font=("Arial", 14),
                     command=play_audio, bg="green", fg="white")
btn_play.pack(pady=5)

btn_recognize = tk.Button(root, text="🤖 Распознать речь", font=("Arial", 14),
                          command=recognize_speech, bg="blue", fg="white")
btn_recognize.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380)
result_label.pack(pady=10)

root.mainloop()
