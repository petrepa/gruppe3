import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
import time
import datetime
from kivy.uix.slider import Slider
import requests


#bestemmer størrelsen til vinduet som åpnes
#from kivy.config import Config
#Config.set('graphics', 'width', '1800')
#Config.set('graphics', 'height', '950')
#Config.write()

#TODO: legge til adresse for bilde og lyd i kv fila

sliderVerdier=[122,122,122]
knappeVerdier=[0,0,255]
checkLastInteraction = 3
LEDadresseString = '/lightall'
RGBstring = '/0/0/255'
LYDadresseString = '/sound/default'
BILDEadresseString = '/picture/default'
valgtLED = 10
valgtBILDE = 10
valgtLYD = 10

#LabelBase.register(name= 'AncientMedium', fn_regular= 'AncientMedium.ttf')
#Funksjonane til framskjerm og menyen
class FrontScreen(Screen):
	pass


class CustomParkControl(Screen):


    #colorSelected tar inn RGB fra knappen med farger og lagrere de i en liste
    def colorSelected(self,r,g,b):
        knappeVerdier[0] = r
        knappeVerdier[1] = g
        knappeVerdier[2] = b
        #print(knappeVerdier[0])

        #s = 'RGB verdiene: R = ' + repr(knappeVerdier[0]) + ', G = ' + repr(knappeVerdier[1]) + ' og B = ' + repr(knappeVerdier[2])
        #print(s)


    # sliderValue tar inn RGB fra sliderene og lagrere de i en liste. id1 = rød, id2 = grønn, id3 = blå
    def sliderValue(self,id,sr):
        if id == 1:
            sliderVerdier[0] = sr
        elif id == 2:
            sliderVerdier[1] = sr
        elif id == 3:
            sliderVerdier[2] = sr

        #s = 'RGB slider: R = ' + repr(sliderVerdier[0]) + ', G = ' + repr(sliderVerdier[1]) + ' og B = ' + repr(sliderVerdier[2])
        #print(s)


    #sjekker om det er RGB verdiene til knappen eller sliderene
    #som skal sendes til server. 0 = knapp og 1 = slider
    def lastButtonIneraction(self,id):
        global checkLastInteraction
        global RGBstring
        if id == 0:
            checkLastInteraction = 1
            RGBstring = '/' + str(knappeVerdier[0]) + '/' + str(knappeVerdier[1]) + '/' + str(knappeVerdier[2])
            #print(RGBstring)
        elif id == 1:
            #time.sleep(1)
            #for loop som sjekker om verdien har endret seg de
            #siste 10 sekundene?
            checkLastInteraction = 2
            RGBstring = '/' + str(sliderVerdier[0]) + '/' + str(sliderVerdier[1]) + '/' + str(sliderVerdier[2])
            #print (RGBstring)
        else:
            RGBstring = '/' + str(0) + '/' + str(0) + '/' + str(255)
        #kaller på sendToServer og åpner nettsiden og sender infoen
        # ved å kalle den her blir det ikke rot om man bytter LED
        sm = CustomParkControl()
        sm.sendToServer()


    #Siden toggle knappen reagerer på både av og på må vi filtrere ut verdien som blir sendt når
    #knappen slår seg av. Dersom alle knappene er av blir den automatisk sett til "ALLE" = 10
    def selectedLED(self, id):
        global valgtLED
        global LEDadresseString
        if id == 1:
            if valgtLED == 1:
                valgtLED = 10
                #print('her' + str(valgtLED))
                LEDadresseString = '/lightall'
                #print(LEDadresseString)
            else:
                valgtLED = 1
                LEDadresseString = '/lightsingle/1'
                #print(LEDadresseString)
        elif id == 11:
            if valgtLED == 11:
                valgtLED = 10
                LEDadresseString = '/lightall'
                #print(str(id) + ' = ' + str(valgtLED))
            else:
                valgtLED = 11
                LEDadresseString = '/lightsingle/11'
                #print(LEDadresseString)
        elif id == 21:
            if valgtLED == 21:
                valgtLED = 10
                LEDadresseString = '/lightall'
                #print(str(id) + ' = ' + str(valgtLED))
            else:
                valgtLED = 21
                LEDadresseString = '/lightsingle/21'
                #print(LEDadresseString)
        elif id == 31:
            if valgtLED == 31:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 31
                LEDadresseString = '/lightsingle/31'
        elif id == 41:
            if valgtLED == 41:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 41
                LEDadresseString = '/lightsingle/41'
        elif id == 51:
            if valgtLED == 51:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 51
                LEDadresseString = '/lightsingle/51'
        elif id == 61:
            if valgtLED == 61:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 61
                LEDadresseString = '/lightsingle/61'
        elif id == 71:
            if valgtLED == 71:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 71
                LEDadresseString = '/lightsingle/71'
        elif id == 81:
            if valgtLED == 81:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 81
                LEDadresseString = '/lightsingle/81'
        elif id == 91:
            if valgtLED == 91:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 91
                LEDadresseString = '/lightsingle/91'
        else:
            valgtLED = 10
            LEDadresseString = '/lightall'


    def selectedSound(self, id):
        global valgtLYD
        global LYDadresseString
        if id == 1:
            if valgtLYD == 1:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
                #print('id1 ' + str(valgtLYD))
            else:
                valgtLYD = 1
                LYDadresseString = '/sound/fuglekvitter1'
                #print(LYDadresseString)
        elif id == 2:
            if valgtLYD == 2:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
                #print('id2 ' + str(valgtLYD))
            else:
                valgtLYD = 2
                LYDadresseString = '/sound/fuglekvitter2'
                #print(LYDadresseString)
        elif id == 3:
            if valgtLYD == 3:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 3
                LYDadresseString = '/sound/fuglekvitter3'
        elif id == 4:
            if valgtLYD == 4:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 4
                LYDadresseString = '/sound/fuglekvitter4'
        elif id == 5:
            if valgtLYD == 5:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 5
                LYDadresseString = '/sound/fuglekvitter5'
        elif id == 6:
            if valgtLYD == 6:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 6
                LYDadresseString = '/sound/fuglekvitter6'
        elif id == 7:
            if valgtLYD == 7:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 7
                LYDadresseString = '/sound/fuglekvitter7'
        else:
            LYDadresseString = '/sound/default'
            #print(LYDadresseString)
        sm = CustomParkControl()
        sm.sendToServer()


    def selectedPicture(self, id):
        global valgtBILDE
        global BILDEadresseString
        if id == 1:
            if valgtBILDE == 1:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
                #print('id1 ' + str(valgtBILDE))
            else:
                valgtBILDE = 1
                BILDEadresseString = '/picture/orken1'
                #print(BILDEadresseString)
        elif id == 2:
            if valgtBILDE == 2:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 2
                BILDEadresseString = '/picture/orken2'
        elif id == 3:
            if valgtBILDE == 3:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 3
                BILDEadresseString = '/picture/orken3'
        elif id == 4:
            if valgtBILDE == 4:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 4
                BILDEadresseString = '/picture/orken4'
        elif id == 5:
            if valgtBILDE == 5:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 5
                BILDEadresseString = '/picture/orken5'
        elif id == 6:
            if valgtBILDE == 6:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 6
                BILDEadresseString = '/picture/orken6'
        elif id == 7:
            if valgtBILDE == 7:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 7
                BILDEadresseString = '/picture/orken7'
        else:
            BILDEadresseString = '/picture/default'
        sm = CustomParkControl()
        sm.sendToServer()


    def sendToServer(self):
        global valgtLED
        global adresseString
        global LEDadresseString
        global RGBstring
        global BILDEadresseString
        global LYDadresseString
        klokkenNu = datetime.datetime.now() #henter va klokken er nå
        tidStopMusikk = klokkenNu.replace(hour=12, minute=3, second=0, microsecond=0)
        if klokkenNu > tidStopMusikk:
            adresseString = 'http://192.168.1.10:8080' + LEDadresseString + RGBstring + BILDEadresseString
            print(adresseString)
            #r = requests.get(adresseString)
        else:
            adresseString = 'http://192.168.1.10:8080' + LEDadresseString + RGBstring + LYDadresseString + BILDEadresseString
            print(adresseString)
            #r = requests.get(adresseString)


class ScreenManagement(ScreenManager):
	pass

presentation = Builder.load_file("myFrontKlima.kv")

class myApp(App):
    def build(self):
        return presentation

if __name__=="__main__":
	myApp().run()