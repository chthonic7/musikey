import re
import sys
import subprocess
from myaudio import MyAudio
# from pydub.playback import play
# from pydub import AudioSegment
# from pydub.generators import Sine

win = subprocess.Popen(["xinput", "test", str(10)], stdout=subprocess.PIPE)

a = MyAudio(440)
b = MyAudio(493.88)
c = MyAudio(523.25)
d = MyAudio(587.33)
e = MyAudio(659.25)
f = MyAudio(698.46)
g = MyAudio(783.99)
all = [a,b,c,d,e,f,g]

regices = {'a' : '38',
           'b' : '56',
           'c' : '54',
           'd' : '40',
           'e' : '26',
           'f' : '41',
           'g' : '42',
           'h' : '43',
           'i' : '31',
           'j' : '44',
           'k' : '45',
           'l' : '58',
           'm' : '58',
           'n' : '57',
           'o' : '32',
           'p' : '33',
           'q' : '24',
           'r' : '27',
           's' : '39',
           't' : '28',
           'u' : '30',
           'v' : '55',
           'w' : '25',
           'x' : '53',
           'y' : '29',
           'z' : '52',
           'shift' : '50',
           'ctl' : '37',
           }
switch = {'p' : 'press', 'r' : 'release'}

def regex(toggle,val):
        return switch[toggle]+'( )*'+regices[val]

for lin in win.stdout:
        line = lin.decode("utf-8")
        if re.search(regex('p','a'),line):
                a.start_playback()
        elif re.search(regex('r','a'),line):
                a.stop_playback()
        elif re.search(regex('p','b'),line):
                b.start_playback()
        elif re.search(regex('r','b'),line):
                b.stop_playback()
        elif re.search(regex('p','c'),line):
                c.start_playback()
        elif re.search(regex('r','c'),line):
                c.stop_playback()
        elif re.search(regex('p','d'),line):
                d.start_playback()
        elif re.search(regex('r','d'),line):
                d.stop_playback()
        elif re.search(regex('p','e'),line):
                e.start_playback()
        elif re.search(regex('r','e'),line):
                e.stop_playback()
        elif re.search(regex('p','f'),line):
                f.start_playback()
        elif re.search(regex('r','f'),line):
                f.stop_playback()
        elif re.search(regex('p','g'),line):
                g.start_playback()
        elif re.search(regex('r','g'),line):
                g.stop_playback()
        elif re.search(regex('p','q'),line):
                break
        elif re.search(regex('p','shift'),line):
                for i in all: i.doubleFreq()
        elif re.search(regex('r','shift'),line):
                for i in all: i.halfFreq()
        elif re.search(regex('p','ctl'),line):
                for i in all: i.halfFreq()
        elif re.search(regex('r','ctl'),line):
                for i in all: i.doubleFreq()
        else:
                print(line)
        sys.stdout.flush()
