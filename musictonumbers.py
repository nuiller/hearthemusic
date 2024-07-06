from pydub import AudioSegment
import numpy as np

# load mp3
audio = AudioSegment.from_mp3("music.mp3")

# Convert to raw audio data
samples = np.array(audio.get_array_of_samples())

#save the numbers to txt
with open("list.txt", "w") as file:
    for sample in samples:
        file.write(f"{sample}\n")
