import os

from pydub import AudioSegment
import array
import math

def create_audio_file(decimals_list, output_filename):
    # Normalize decimal values to between 0 and 1
    max_val = max(decimals_list)
    min_val = min(decimals_list)
    decimals_list = [(x - min_val) / (max_val - min_val) for x in decimals_list]

    # Scale the normalized values to the range of a 16-bit signed integer
    int_values = [int((x-0.5) * 32767) for x in decimals_list]

    # Convert the integer values to bytes
    byte_values = array.array('h', int_values).tobytes()

    # Create an AudioSegment from the byte values
    audio_segment = AudioSegment(
        data=byte_values,
        sample_width=2,  # 2 bytes per sample (16-bit signed integer)
        frame_rate=44100,  # 44.1 kHz sample rate
        channels=1  # Mono audio
    )

    # Export the audio segment to a WAV file
    audio_segment.export(output_filename, format="wav")

def f(x):
    # lengthener = 0.1 # The tinier the value the longer the sample
    # common_amp = 1
    # amplitude1 = -2.4
    # pulse1 = .6
    # amplitude2 = -1.3
    # pulse2 = 1
    lengthener = 0.3
    common_amp = 1
    amplitude1 = 3.5
    pulse1 = 1
    amplitude2 = 3
    pulse2 = 1
    return common_amp * amplitude1 * math.sin(lengthener * pulse1 * x + common_amp * amplitude2 * math.sin(lengthener * pulse2 * x))

try:
    os.remove("output.wav")
except FileNotFoundError:
    pass
decimals = [f(x) for x in range(50*157)]
create_audio_file(decimals, "output.wav")
