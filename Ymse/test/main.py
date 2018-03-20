import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class StartScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class mainApp(App):

	def build(self):
	    return StartScreen()

if __name__=='__main__':
    mainApp().run()