#definerer at vi skal bruke kivy
import kivy

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