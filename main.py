#definerer at vi skal bruke kivy
import kivy
import random

#ulike bibliotek importert fra kivy
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
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView




#Funksjonane til framskjerm og menyen
class FrontScreen(Screen):
	pass

class MainWidget(Screen):
	pass


#Funksjonane til dei ulike modulane
class KlimaScreen(Screen):
	S = SoundLoader.load('klimalyd/basseng.mp3')
	def playsS(self):
	    if KlimaScreen.S.state == 'stop':
	        KlimaScreen.S.play()
	    else:
	        KlimaScreen.S.stop()
	H = SoundLoader.load('klimalyd/hav.mp3')
	def playsH(self):
	    if KlimaScreen.H.state == 'stop':
	        KlimaScreen.H.play()
	    else:
	        KlimaScreen.H.stop()
	J = SoundLoader.load('klimalyd/jungel.mp3')
	def playsJ(self):
	    if KlimaScreen.J.state == 'stop':
	        KlimaScreen.J.play()
	    else:
	        KlimaScreen.J.stop()
	I = SoundLoader.load('klimalyd/hav.mp3')
	def playsI(self):
	    if KlimaScreen.I.state == 'stop':
	        KlimaScreen.I.play()
	    else:
	        KlimaScreen.I.stop()

	def stopAll(self):
		if KlimaScreen.S.state == 'play':
			KlimaScreen.S.stop()
		if KlimaScreen.H.state == 'play':
			KlimaScreen.H.stop()
		if KlimaScreen.J.state == 'play':
			KlimaScreen.J.stop()
		if KlimaScreen.I.state == 'play':
			KlimaScreen.I.stop()
	

class HistorieScreen(Screen):
	pass

class SeverdigScreen(Screen):
	pass

class AnnaScreen(Screen):
	pass


class Veibeskrivelser(Screen):
	pass


class Museum(Screen):
	pass

class Rockheim(Screen):
	pass

class TrondelagFolkemuseum(Screen):
	pass

class RingveMuseum(Screen):
	pass

class Vitenskapsmuseet(Screen):
	pass

class Rustkammeret(Screen):
	pass

class NordenfjeldskeKunst(Screen):
	pass

class NorskeDovemuseum(Screen):
	pass

class TrondheimKunstmuseum(Screen):
	pass

class JodiskeMuseum(Screen):
	pass

class TrondheimSjofartsmuseum(Screen):
	pass




class HistoriskeSteder(Screen):
	pass

class Nidarosdomen(Screen):
	pass

class Stiftsgarden(Screen):
	pass

class GamleBybro(Screen):
	pass

class KristianstenFestning(Screen):
	pass

class Erkebispegarden(Screen):
	pass

class Munkholmen(Screen):
	pass

class Bakklandet(Screen):
	pass

class VarFrueKirke(Screen):
	pass



class Kultur(Screen):
	pass

class Vitensenteret(Screen):
	pass

class KunsthallTrondheim(Screen):
	pass

class LitteraturhusetTrondheim(Screen):
	pass

class KultursenteretISAK(Screen):
	pass



class Natur(Screen):
	pass

class Burmaklippen(Screen):
	pass

class Geitfjellet(Screen):
	pass

class Vattakammen(Screen):
	pass

class Ladestien(Screen):
	pass



class MatDrikke(Screen):
	pass

class Tyholttarnet(Screen):
	pass

class IlaBrannstasjon(Screen):
	pass

class Antikvariatet(Screen):
	pass

class ArvesolvetFolkekafe(Screen):
	pass

class CafeNim(Screen):
	pass

class CafeNiMuser(Screen):
	pass

class RosenborgDampbakeri(Screen):
	pass

class SellenraaBokBar(Screen):
	pass

class TrondheimMikrobryggeri(Screen):
	pass

class CafeLokka(Screen):
	pass

class BakklandetSkydsstasjon(Screen):
	pass



class Aktiviteter(Screen):
	pass

class Klatresenter(Screen):
	pass

class Turnhall(Screen):
	pass

class Bowling(Screen):
	pass

class Trampolinepark(Screen):
	pass

class GokartOgLazerx(Screen):
	pass

class EscapeReality(Screen):
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
        liste_mu = ['rockheim', 'trondelagFolkemuseum',
                    'ringveMuseum', 'vitenskapsmuseet', 
                    'rustkammeret', 'nordenfjeldskeKunst',
                    'norskeDovemuseum', 'trondheimKunstmuseum',
                    'jodiskeMuseum', 'trondheimSjofartsmuseum']
        liste_h = ['nidarosdomen', 'stiftsgarden',
                   'gamleBybro', 'kristianstenFestning',
                   'erkebispegarden', 'munkholmen',
                   'bakklandet', 'varFrueKirke']
        liste_k = ['vitensenteret', 'kunsthallTrondheim',
                   'litteraturhusetTrondheim', 'kultursenteretISAK']
        liste_n = ['burmaklippen', 'geitfjellet',
                   'vattakammen', 'ladestien']
        liste_ma = ['tyholttarnet', 'ilaBrannstasjon',
                    'antikvariatet', 'arvesolvetFolkekafe',
                    'cafeNim', 'cafeNiMuser',
                    'rosenborgDampbakeri', 'sellenraaBokBar',
                    'trondheimMikrobryggeri', 'cafeLokka',
                    'bakklandetSkydsstasjon']
        liste_a = ['klatresenter', 'turnhall',
                   'bowling', 'trampolinepark',
                   'gokartOgLazerx', 'escapeReality']
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
            number = random.randint(0, antallSkjermer)
        else:
            number = random.randint(0, len(self.serverdigheter))

        self.testScreen = self.serverdigheter[number]
        return self.testScreen


class ScreenManagement(ScreenManager):
	pass


#Her definerer vi at vi henter inn den tilhøyrande kivy-fila
presentation = Builder.load_file("my.kv")

#klassa som bygger sjølve applikasjonen
class myApp(App):
	def build(self):
		return presentation

#noko magisk som gjer at ting fungerer
if __name__=="__main__":
	myApp().run()
