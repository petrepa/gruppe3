from bottle import route, run, template
import sounddevice as sd
import soundfile as sf
from random import randint
from lib.StupidArtnet import StupidArtnet

import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

@route('/')
def menu():
    return template('menu')


@route('/lightrandom/<address>')
def lightrandom(address):
    return lightsingle(address, randint(0, 255), randint(0, 255), randint(0, 255))

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
    a.show()
    return "OK"

@route('/lightallrandom')
def allrandom():
    a.set_rgb(1,  randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(11, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(21, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(31, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(41, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(51, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(61, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(71, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(81, randint(0, 255), randint(0, 255), randint(0, 255))
    a.set_rgb(91, randint(0, 255), randint(0, 255), randint(0, 255))
    a.show()
    return "OK"

@route('/lightsingle/<address>/<r>/<g>/<b>')
def lightsingle(address, r, g, b):
    address = int(address) # 1 - 11 - 21 - 31- 41 - 51 - 61 - 71 - 81 - 91

    # SET THE ARTNET BUFFER TO OUR DATA ...
    a.set_rgb(address, r, g, b)

    # ... AND SEND
    a.show()

    return "OK"

@route('/sound/<tittel>')
def sound(speaker):
    speaker = 1 #setter at alle høytalerene spiller av
    data, fs = sf.read('tittel.wav', dtype='float32')

    # To see available sound devices, use python3 -m sounddevice
    sd.default.device = '24Ao'
    #sd.default.device = 'Built-in Output' # OS x default

    mono = [(sample[0]+sample[1])/2 for sample in data]; #convert to mono

    speaker = int(speaker)
    sd.play(mono, fs, mapping=[speaker], blocking=False) # remove mapping argument to test on machines without fancy soundcard
    return "OK"

@route('/picture/<tittel>')
def bilde():
    pilImage = Image.open("tittel.png")
    showPIL(pilImage)
return "OK"



# VALUES SET FOR THE ADRESSAPARKEN FIXED INSTALL
target_ip = '192.168.1.10'  # typically in 2.x or 10.x range
universe = 0                # see docs
packet_size = 100           # it is not necessary to send whole universe

# CREATING A STUPID ARTNET OBJECT
a = StupidArtnet()

# SETUP NEEDS FEW SKIPPABLE ELEMENTS, WE DEFINED ABOVE
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
a.setup(target_ip, universe, packet_size)
print(a)

run(host='0.0.0.0', port=8080)