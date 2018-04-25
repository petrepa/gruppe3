#definerer at vi skal bruke kivy, samt andre bibliotek
import kivy
import random
import time
import datetime
#import requests


#ulike bibliotek importert fra kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader,Sound
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.uix.slider import Slider
from kivy.network.urlrequest import UrlRequest


#Funksjonane til framskjerm og menyen
class FrontScreen(Screen):
	pass

class MainWidget(Screen):
	pass


#Funksjonane til dei ulike modulane
class KlimaScreen(Screen):
   pass
'''
    def syden(self):
        UrlRequest('http://192.168.1.3:8080/Picture/syden') #Bilde
        UrlRequest('http://192.168.1.3:8080/Sound/syden') #Lyd
        UrlRequest('http://192.168.1.3:8080/lightall/') #Lys
'''
	

class HistorieScreen(Screen):
	pass

class SeverdigScreen(Screen):
	pass

class Veibeskrivelser(Screen):
	pass

class KulturScreen(Screen):
	pass

class Museum(Screen):
	pass

class Rockheim(Screen):
	pass
class RockheimInfo(Screen):
	pass

class TrondelagFolkemuseum(Screen):
	pass
class TrondelagFolkemuseumInfo(Screen):
    pass

class RingveMuseum(Screen):
	pass
class RingveMuseumInfo(Screen):
    pass

class Vitenskapsmuseet(Screen):
	pass
class VitenskapsmuseetInfo(Screen):
    pass

class Rustkammeret(Screen):
	pass
class RustkammeretInfo(Screen):
    pass

class NordenfjeldskeKunst(Screen):
	pass
class NordenfjeldskeKunstInfo(Screen):
	pass

class NorskeDovemuseum(Screen):
	pass
class NorskDovemuseumInfo(Screen):
	pass

class TrondheimKunstmuseum(Screen):
	pass
class TrondheimKunstmuseumInfo(Screen):
	pass

class JodiskeMuseum(Screen):
	pass
class JodiskMuseumInfo(Screen):
	pass

class TrondheimSjofartsmuseum(Screen):
	pass
class TrondheimSjofartsmuseumInfo(Screen):
	pass




class HistoriskeSteder(Screen):
	pass

class Nidarosdomen(Screen):
	pass
class NidarosdomenInfo(Screen):
	pass

class Stiftsgarden(Screen):
	pass
class StiftsgardenInfo(Screen):
	pass

class GamleBybro(Screen):
	pass
class GamleBybroInfo(Screen):
	pass

class KristianstenFestning(Screen):
	pass
class KristianstenFestningInfo(Screen):
	pass

class Erkebispegarden(Screen):
	pass
class ErkebispegardenInfo(Screen):
	pass

class Munkholmen(Screen):
	pass
class MunkholmenInfo(Screen):
	pass

class Bakklandet(Screen):
	pass
class BakklandetInfo(Screen):
	pass

class VarFrueKirke(Screen):
	pass
class VarFrueKirkeInfo(Screen):
	pass



class Kultur(Screen):
	pass

class Vitensenteret(Screen):
	pass
class VitensenteretInfo(Screen):
	pass

class KunsthallTrondheim(Screen):
	pass
class KunsthallTrondheimInfo(Screen):
	pass

class LitteraturhusetTrondheim(Screen):
	pass
class LitteraturhusetTrondheimInfo(Screen):
	pass

class KultursenteretISAK(Screen):
	pass
class KultursenteretISAKInfo(Screen):
	pass


class Natur(Screen):
	pass

class Burmaklippen(Screen):
	pass
class BurmaklippenInfo(Screen):
	pass

class Geitfjellet(Screen):
	pass
class GeitfjelletInfo(Screen):
	pass

class Vattakammen(Screen):
	pass
class VattakammenInfo(Screen):
	pass

class Ladestien(Screen):
	pass
class LadestienInfo(Screen):
	pass



class MatDrikke(Screen):
	pass

class Tyholttarnet(Screen):
	pass
class TyholttarnetInfo(Screen):
	pass

class IlaBrannstasjon(Screen):
	pass
class IlaBrannstasjonInfo(Screen):
	pass

class Antikvariatet(Screen):
	pass
class AntikvariatetInfo(Screen):
	pass

class ArvesolvetFolkekafe(Screen):
	pass
class ArvesolvetFolkekafeInfo(Screen):
	pass

class CafeNim(Screen):
	pass
class CafeNimInfo(Screen):
	pass


class CafeNiMuser(Screen):
	pass
class CafeNiMuserInfo(Screen):
	pass

class RosenborgDampbakeri(Screen):
	pass
class RosenborgDampbakeriInfo(Screen):
	pass

class SellenraaBokBar(Screen):
	pass
class SellenraaBokBarInfo(Screen):
	pass

class TrondheimMikrobryggeri(Screen):
	pass
class TrondheimMikrobryggeriInfo(Screen):
	pass

class CafeLokka(Screen):
	pass
class CafeLokkaInfo(Screen):
	pass


class BakklandetSkydsstasjon(Screen):
	pass
class BakklandetSkydsstasjonInfo(Screen):
	pass



class Aktiviteter(Screen):
	pass

class Klatresenter(Screen):
	pass
class KlatresenterInfo(Screen):
	pass

class Turnhall(Screen):
	pass
class TurnhallInfo(Screen):
	pass

class Bowling(Screen):
	pass
class BowlingInfo(Screen):
	pass

class Trampolinepark(Screen):
	pass
class TrampolineparkInfo(Screen):
	pass

class GokartOgLazerx(Screen):
	pass
class GokartOgLazerxInfo(Screen):
	pass

class EscapeReality(Screen):
	pass
class EscapeRealityInfo(Screen):
	pass


class SelectionScreen(Screen):
    testScreen = StringProperty('Screen1')

    checbox_is_active = ObjectProperty(False)
    serverdigheter = []
    museum = 0
    historisk = 0
    kultur = 0
    natur = 0
    mat = 0
    aktiviteter = 0

    def checkbox_museum_cliked(self, instance, value):
        if value is True:
            print("Checkbox 1 Checked")
            self.museum = 1
        else:
            print("Checkbox 1 is Unchecked")
            self.museum = 0
    def checkbox_historisk_cliked(self, instance, value):
        if value is True:
            print("Checkbox 2 Checked")
            self.historisk = 1
        else:
            print("Checkbox 2 is Unchecked")
            self.historisk = 0
    def checkbox_kultur_cliked(self, instance, value):
        if value is True:
            print("Checkbox 3 Checked")
            self.kultur = 1
        else:
            print("Checkbox 3 is Unchecked")
            self.kultur = 0
    def checkbox_natur_cliked(self, instance, value):
        if value is True:
            print("Checkbox 4 Checked")
            self.natur = 1
        else:
            print("Checkbox 4 is Unchecked")
            self.natur = 0
    def checkbox_mat_cliked(self, instance, value):
        if value is True:
            print("Checkbox 5 Checked")
            self.mat = 1
        else:
            print("Checkbox 5 is Unchecked")
            self.mat = 0
    def checkbox_aktiviteter_cliked(self, instance, value):
        if value is True:
            print("Checkbox 6 Checked")
            self.aktiviteter = 1
        else:
            print("Checkbox 6 is Unchecked")
            self.aktiviteter = 0

    def screenSelector(self):
        self.serverdigheter = []
        liste_mu = ['rockheiminfo', 'trondelagfolkemuseuminfo',
                    'ringvemuseuminfo', 'vitenskapsmuseetinfo',
                    'rustkammeretinfo', 'nordenfjeldskekunstinfo',
                    'norskdovemuseuminfo', 'trondheimkunstmuseuminfo',
                    'jodiskmuseuminfo', 'trondheimsjofartsmuseuminfo']
        liste_h = ['nidarosdomeninfo', 'stiftsgardeninfo',
                   'gamlebybroinfo', 'kristianstenfestninginfo',
                   'erkebispegardeninfo', 'munkholmeninfo',
                   'bakklandetinfo', 'varfruekirkeinfo']
        liste_k = ['vitensenteretinfo', 'kunsthalltrondheiminfo',
                   'litteraturhusettrondheiminfo', 'kultursenteretISAKinfo']
        liste_n = ['burmaklippeninfo', 'geitfjelletinfo',
                   'vattakammeninfo', 'ladestieninfo']
        liste_ma = ['tyholttarnetinfo', 'ilabrannstasjoninfo',
                    'antikvariatetinfo', 'arvesolvetfolkekafeinfo',
                    'cafeniminfo', 'cafenimuserinfo',
                    'rosenborgdampbakeriinfo', 'sellenraabokbarinfo',
                    'trondheimmikrobryggeriinfo', 'cafelokkainfo',
                    'bakklandetskydsstasjoninfo']
        liste_a = ['klatresenterinfo', 'turnhallinfo',
                   'bowlinginfo', 'trampolineparkinfo',
                   'gokartoglazerxinfo', 'escaperealityinfo']
        antallSkjermer = 43

        if int(self.museum) == 1:
            self.serverdigheter.extend(liste_mu)
            print("Museum i liste")
        if int(self.historisk) == 1:
            self.serverdigheter.extend(liste_h)
            print("Historisk i liste")
        if int(self.kultur) == 1:
            self.serverdigheter.extend(liste_k)
            print("Kultur i liste")
        if int(self.natur) == 1:
            self.serverdigheter.extend(liste_n)
            print("Natur i liste")
        if int(self.mat) == 1:
            self.serverdigheter.extend(liste_ma)
            print("Mat i liste")
        if int(self.aktiviteter) == 1:
            self.serverdigheter.extend(liste_a)
            print("Aktiviteter i liste")

        if not self.serverdigheter:
            number = random.randint(0, antallSkjermer-1)
            self.serverdigheter.extend(liste_mu)
            self.serverdigheter.extend(liste_h)
            self.serverdigheter.extend(liste_k)
            self.serverdigheter.extend(liste_n)
            self.serverdigheter.extend(liste_ma)
            self.serverdigheter.extend(liste_a)
        else:
            number = random.randint(0, len(self.serverdigheter)-1)

        self.testScreen = self.serverdigheter[number]
        return self.testScreen

#------------------------------------------------------------------------------------
# Parkkontroll
#------------------------------------------------------------------------------------
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
timeNarLydSlasAv = 23
minNarLydSlasAv = 0


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


    # sliderValue tar inn RGB fra sliderene og lagrere de i en liste. id1 = rød, id2 = grønn, id3 = blå
    def sliderValue(self,id,sr):
        if id == 1:
            sliderVerdier[0] = sr
        elif id == 2:
            sliderVerdier[1] = sr
        elif id == 3:
            sliderVerdier[2] = sr


    #sjekker om det er RGB verdiene til knappen eller sliderene
    #som skal sendes til server. 0 = knapp og 1 = slider
    def lastButtonIneraction(self,id):
        global checkLastInteraction
        global RGBstring
        #Sjekker om det er knappene for fargevalg som e brukt sist
        if id == 0:
            checkLastInteraction = 1
            RGBstring = '/' + str(knappeVerdier[0]) + '/' + str(knappeVerdier[1]) + '/' + str(knappeVerdier[2])
            adresseString = 'http://192.168.1.3:8080' + LEDadresseString + RGBstring
            #r = requests.get(adresseString)
            UrlRequest(adresseString)
            #print('LED: ' + adresseString)

        #Sjekker om det er sliderene for fargevalg som e brukt sist
        elif id == 1:
            checkLastInteraction = 2
            RGBstring = '/' + str(sliderVerdier[0]) + '/' + str(sliderVerdier[1]) + '/' + str(sliderVerdier[2])
            adresseString = 'http://192.168.1.3:8080' + LEDadresseString + RGBstring
            #r = requests.get(adresseString)
            #print('LED: ' + adresseString)
            UrlRequest(adresseString)
        else:
            RGBstring = '/' + str(0) + '/' + str(0) + '/' + str(255)


    #Siden toggle knappen reagerer på både av og på må vi filtrere ut verdien som blir sendt når
    #knappen slår seg av. Dersom alle knappene er av blir den automatisk sett til "ALLE" = 10
    def selectedLED(self, id):
        global valgtLED
        global LEDadresseString
        if id == 1:
            if valgtLED == 1:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 1
                LEDadresseString = '/lightsingle/1'
        elif id == 11:
            if valgtLED == 11:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 11
                LEDadresseString = '/lightsingle/11'
        elif id == 21:
            if valgtLED == 21:
                valgtLED = 10
                LEDadresseString = '/lightall'
            else:
                valgtLED = 21
                LEDadresseString = '/lightsingle/21'
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
        global timeNarLydSlasAv
        global minNarLydSlasAv
        if id == 1:
            if valgtLYD == 1:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 1
                LYDadresseString = '/sound/fuglekvitter1'
        elif id == 2:
            if valgtLYD == 2:
                valgtLYD = 10
                LYDadresseString = '/sound/default'
            else:
                valgtLYD = 2
                LYDadresseString = '/sound/fuglekvitter2'
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

        klokkenNu = datetime.datetime.now()  # henter va klokken er nå
        tidStopMusikk = klokkenNu.replace(hour=timeNarLydSlasAv, minute=minNarLydSlasAv, second=0, microsecond=0)
        if klokkenNu < tidStopMusikk:
            adresseString = 'http://192.168.1.3:8080' + LYDadresseString
            #r = requests.get(adresseString)
            UrlRequest(adresseString)
            #print('LYD: ' + adresseString)



    def selectedPicture(self, id):
        global valgtBILDE
        global BILDEadresseString
        if id == 1:
            if valgtBILDE == 1:
                valgtBILDE = 10
                BILDEadresseString = '/picture/default'
            else:
                valgtBILDE = 1
                BILDEadresseString = '/picture/orken1'
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
            
        adresseString = 'http://192.168.1.3:8080' + BILDEadresseString
        adresseStringMAC2 = 'http://192.168.1.4:8080' + BILDEadresseString
        UrlRequest(adresseString)
        UrlRequest(adresseStringMAC2)
        #print('BILDE: ' + adresseString)






class ScreenManagement(ScreenManager):
	pass


#Her definerer vi at vi henter inn den tilhøyrande kivy-fila
#presentation = Builder.load_file("my.kv")
with open("my.kv", encoding='utf8') as f:
 presentation = Builder.load_string(f.read())


#klassa som bygger sjølve applikasjonen
class myApp(App):
	def build(self):
		return presentation

#noko magisk som gjer at ting fungerer
if __name__=="__main__":
	myApp().run()
