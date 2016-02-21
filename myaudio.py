import math
import array
import itertools
import pyaudio

class MyAudio(object):
    def __init__(self, freq, volume = -10.0, sample_rate=44100, bit_depth=16):
        self.sample_rate=sample_rate
        self.bit_depth=bit_depth
        self.freq=freq
        self.volume = volume
        self.p = pyaudio.PyAudio()
        # frame width for 16-bit is 2
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
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
            yield math.sin(sine_of * self.sample_n)
            self.sample_n += 1

    def callback(self, in_data, frame_count, time_info, status):
        #minVal, maxVal = get_min_max_value(self.bit_depth)
        #for 16-bit audio, maxVal = 0x7fff
        maxVal = 0x7fff
        gain = 10 ** (self.volume / 20)
        stream_data = (int(val * maxVal * gain) for val in self.generate())
        idata = itertools.islice(stream_data, 0, frame_count)
        # array_type for 16-bit is "h"
        data = array.array("h", idata)
        return (data.tostring(),pyaudio.paContinue)

    def start_playback(self):
        self.stream.start_stream()

    def stop_playback(self):
        self.stream.stop_stream()

    def doubleFreq(self):
        self.freq *= 2

    def halfFreq(self):
        self.freq /= 2
