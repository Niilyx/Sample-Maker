import os

from pydub import AudioSegment
import array
import math

def downsample(in_file, output_filename, force=4):
    if force > 3:
        print(f"Force value of {force} is way high, the audio may be unrecognizable.")

    # Load the audio file
    audio = AudioSegment.from_file(in_file)

    # Get the raw data from the audio file
    raw_data = audio.raw_data

    # Convert the raw data to an array of integers
    int_values = array.array('h', raw_data)
    for i in range(len(int_values)):
        int_values[i] = int_values[i-1] if i % force else int_values[i]

    # Convert the integer values to bytes
    byte_values = array.array('h', int_values).tobytes()

    # Create an AudioSegment from the byte values
    audio_segment = AudioSegment(
        data=byte_values,
        sample_width=2,  # 2 bytes per sample (16-bit signed integer)
        frame_rate=audio.frame_rate,
        channels=1  # Mono audio
    )

    # Export the audio segment to a WAV file
    audio_segment.export(output_filename, format=format)

format = "wav"

f = input("File? ")

if not f:
    f = "99lb.wav"
elif not f.endswith(f".{format}"):
    f += f".{format}"

out_name = ".".join(f.split(".")[:-1]) + "_dsmp"

i = 1
while os.path.exists(f"{out_name}{i}.{format}"): i += 1
downsample(f, f"{out_name}{i}.{format}")
