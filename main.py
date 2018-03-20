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

class Veibeskrivelser(Screen):
	pass

class Museum(Screen):
	pass

class HistoriskeSteder(Screen):
	pass

class Nidarosdomen(Screen):
	pass

class Kultur(Screen):
	pass


class ScreenManagement(ScreenManager):
	pass



presentation = Builder.load_file("my.kv")

class myApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	myApp().run()