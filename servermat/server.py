from bottle import route, run, template
import sounddevice as sd
import soundfile as sf
from random import randint
from lib.StupidArtnet import StupidArtnet
from subprocess import call
import os
from pynput.keyboard import Key, Controller
import cv2
from openImage import displayImage


@route('/')
def menu():
    return template('menu')


@route('/picture/<bilde>')
def picture(bilde):
    displayImage(bilde)
    return "OK"

@route('/sound/<speaker>/<music>')
def sound(speaker, music):
    data, fs = sf.read(music, dtype='float32')

    # To see available sound devices, use python3 -m sounddevice
    sd.default.device = '24Ao'
    #sd.default.device = 'Built-in Output' # OS x default

    mono = [(sample[0]+sample[1])/2 for sample in data]; #convert to mono

    speaker = int(speaker)
    sd.play(mono, fs, mapping=[speaker], blocking=False) # remove mapping argument to test on machines without fancy soundcard
    return "OK"


@route('/lightall/<sr>/<sg>/<sb>')
def allblue(sr, sg, sb):
    r = int(sr)
    g = int(sg)
    b = int(sb)
    a.set_rgb(1, r, g, b)
    a.set_rgb(11, r, g, b)
    a.set_rgb(21, r, g, b)
    a.set_rgb(31, r, g, b)
    a.set_rgb(41, r, g, b)
    a.set_rgb(51, r, g, b)
    a.set_rgb(61, r, g, b)
    a.set_rgb(71, r, g, b)
    a.set_rgb(81, r, g, b)
    a.set_rgb(91, r, g, b)
    return "OK"


@route('/lightsingle/<address>/<sr>/<sg>/<sb>')
def lightsingle(address, sr, sg, sb):
    address = int(address) # 1 - 11 - 21 - 31- 41 - 51 - 61 - 71 - 81 - 91
    r=int(sr)
    g=int(sg)
    b=int(sb)
    # SET THE ARTNET BUFFER TO OUR DATA ...
    a.set_rgb(address, r, g, b)
    return "OK"



# VALUES SET FOR THE ADRESSAPARKEN FIXED INSTALL
target_ip = '192.168.1.10'  # typically in 2.x or 10.x range
packet_size = 100           # it is not necessary to send whole universe
universe = 0


# CREATING A STUPID ARTNET OBJECT
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
a = StupidArtnet(target_ip, universe, packet_size)

# SEE IF EVERYTHING IS OK
print(a)

# START ARTNET THREAD
a.start()

run(host='0.0.0.0', port='8080')
