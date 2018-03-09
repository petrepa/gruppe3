import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder



class MainWidget(Screen):
	pass

class FrontScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

presentation = Builder.load_file("my.kv")

class myApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	myApp().run()