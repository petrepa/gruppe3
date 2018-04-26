import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

class FrontScreen(Screen):
	pass

presentation = Builder.load_file("framskjerm.kv")

class framskjermApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	framskjermApp().run()
