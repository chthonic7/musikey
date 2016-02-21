import re
import sys
import subprocess
from myaudio import MyAudio
# from pydub.playback import play
# from pydub import AudioSegment
# from pydub.generators import Sine

win = subprocess.Popen(["xinput", "test", str(10)], stdout=subprocess.PIPE)

# a = MyAudio(440)
# b = MyAudio(493.88)
# c = MyAudio(523.25)
# d = MyAudio(587.33)
# e = MyAudio(659.25)
# f = MyAudio(698.46)
# g = MyAudio(783.99)
# all = [a,b,c,d,e,f,g]

regices = {'z' : ('52', MyAudio(415.30)),
           'a' : ('38', MyAudio(440)),
           'q' : ('24', MyAudio(466.16)),
           'x' : ('53', MyAudio(466.16)),
           's' : ('39', MyAudio(493.88)),
           'w' : ('25', MyAudio(523.25)),
           'c' : ('54', MyAudio(493.88)),
           'd' : ('40', MyAudio(523.25)),
           'e' : ('26', MyAudio(554.37)),
           'v' : ('55', MyAudio(554.37)),
           'f' : ('41', MyAudio(587.33)),
           'r' : ('27', MyAudio(622.25)),
           'm' : ('58', MyAudio(622.25)),
           'j' : ('44', MyAudio(659.25)),
           'u' : ('30', MyAudio(698.46)),
           ',' : ('59', MyAudio(659.25)),
           'k' : ('45', MyAudio(698.46)),
           'i' : ('31', MyAudio(739.99)),
           '.' : ('60', MyAudio(739.99)),
           'l' : ('46', MyAudio(783.99)),
           'o' : ('32', MyAudio(830.61)),
           '/' : ('61', MyAudio(830.61)),
           ';' : ('47', MyAudio(880)),
           'p' : ('33', MyAudio(932.33)),
           'shift' : ('50',MyAudio(0)),
           'ctl' : ('37', MyAudio(0)),
           ## end of used keybindings
           't' : ('28', MyAudio(0)),
           'y' : ('29', MyAudio(0)),
           'b' : ('56', MyAudio(0)),
           'g' : ('42', MyAudio(0)),
           'h' : ('43', MyAudio(0)),
           'n' : ('57', MyAudio(0)),
           '1' : ('10', MyAudio(0)),
           '2' : ('11', MyAudio(0)),
           '3' : ('12', MyAudio(0)),
           '4' : ('13', MyAudio(0)),
           '5' : ('14', MyAudio(0)),
           '6' : ('15', MyAudio(0)),
           '7' : ('16', MyAudio(0)),
           '8' : ('17', MyAudio(0)),
           '9' : ('18', MyAudio(0)),
           '0' : ('19', MyAudio(0)),
           }
switch = {'p' : 'press', 'r' : 'release'}
def regex(tog, val):
        return switch[tog]+'( )*'+regices[val][0]

def searchy(val,line):
        if re.search('press( )*'+regices[val][0],line):
                regices[val][1].start_playback()
        elif re.search('release( )*'+regices[val][0],line):
                regices[val][1].stop_playback()
        else:
                return False
        return True


for lin in win.stdout:
        line = lin.decode("utf-8")
        if re.search(regex('p', '0'),line):
                break;
        elif re.search(regex('p','shift'),line):
                for k,i in regices.items(): i[1].doubleFreq()
        elif re.search(regex('r','shift'),line):
                for k,i in regices.items(): i[1].halfFreq()
        elif re.search(regex('p','ctl'),line):
                for k,i in regices.items(): i[1].halfFreq()
        elif re.search(regex('r','ctl'),line):
                for k,i in regices.items(): i[1].doubleFreq()
        elif searchy('z',line): None
        elif searchy('a',line): None
        elif searchy('q',line): None
        elif searchy('x',line): None
        elif searchy('s',line): None
        elif searchy('w',line): None
        elif searchy('c',line): None
        elif searchy('d',line): None
        elif searchy('e',line): None
        elif searchy('v',line): None
        elif searchy('f',line): None
        elif searchy('r',line): None
        elif searchy('m',line): None
        elif searchy('j',line): None
        elif searchy('u',line): None
        elif searchy(',',line): None
        elif searchy('k',line): None
        elif searchy('i',line): None
        elif searchy('.',line): None
        elif searchy('l',line): None
        elif searchy('o',line): None
        elif searchy('/',line): None
        elif searchy(';',line): None
        elif searchy('p',line): None
        else:
                print(line)
        sys.stdout.flush()
