from pydub import AudioSegment
import numpy as np
import wave

# NOTICE: you can use any numbers from math, functions, script(music2numbers) and etc.
# read numbers from list.txt
with open("list.txt", "r") as file:
    samples = np.array([int(line.strip()) for line in file], dtype=np.int16)

# Creating audiosegment
frame_rate = 44100  # frame rate
sample_width = samples.dtype.itemsize
channels = 2

# to bytes
audio_data = samples.tobytes()

# wave file creating
with wave.open("reconstructed_music.wav", "w") as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(sample_width)
    wf.setframerate(frame_rate)
    wf.writeframes(audio_data)

# wav to mp3
audio = AudioSegment.from_wav("reconstructed_music.wav")
audio.export("reconstructed_music.mp3", format="mp3")
