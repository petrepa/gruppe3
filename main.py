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


class ScreenManagement(ScreenManager):
	pass



presentation = Builder.load_file("my.kv")

class myApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	myApp().run()