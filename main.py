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








#Funksjonane til framskjerm og menyen
class FrontScreen(Screen):
	pass

class MainWidget(Screen):
	pass


#Funksjonane til dei ulike modulane
class KlimaScreen(Screen):
	M = SoundLoader.load('klimalyd/test.mp3')
	def plays(self):
	    if KlimaScreen.M.state == 'stop':
	        KlimaScreen.M.play()
	    else:
	        KlimaScreen.M.stop()
	

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


#presentation2 = Builder.load_file('button.kv')


presentation = Builder.load_file("my.kv")

class myApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	myApp().run()