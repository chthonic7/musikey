import math
import random
import array
import itertools
import pyaudio
from pydub.utils import *

class MyAudio(object):
    def __init__(self, freq, volume = -10.0, sample_rate=44100, bit_depth=16):
        self.sample_rate=sample_rate
        self.bit_depth=bit_depth
        self.freq=freq
        self.volume = volume
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(get_frame_width(bit_depth)),
                             channels=1,
                             rate=sample_rate,
                             output=True,
                             stream_callback=self.callback)
        self.sample_n=0
        self.stream.start_stream()
        self.stream.stop_stream()

    def generate(self):
        while True:
            sine_of = (self.freq * 2 * math.pi) / self.sample_rate
            sine1_of = ((self.freq*1/4) * 2 * math.pi) / self.sample_rate
            sine2_of = ((self.freq*8/3) * 2 * math.pi) / self.sample_rate
            yield math.sin(sine_of * self.sample_n) + 0.75*math.sin(sine1_of * self.sample_n) + 0.5*math.sin(sine2_of * self.sample_n)
            self.sample_n += 1

    def callback(self, in_data, frame_count, time_info, status):
        minVal, maxVal = get_min_max_value(self.bit_depth)
        gain = db_to_float(self.volume)
        stream_data = (int(val * maxVal * gain) for val in self.generate())
        idata = itertools.islice(stream_data, 0, frame_count)
        data = array.array(get_array_type(self.bit_depth), idata)
        return (data.tostring(),pyaudio.paContinue)

    def start_playback(self):
        self.stream.start_stream()

    def stop_playback(self):
        self.stream.stop_stream()

    def doubleFreq(self):
        self.freq *= 2

    def halfFreq(self):
        self.freq /= 2
