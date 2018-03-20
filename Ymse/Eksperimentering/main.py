from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


import custombutton

class mainApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')


        f = FloatLayout()
        l = Label(text='Adressa',
                  font_size=150)
        btn = Button(text='Trykk på meg',
                  font_size=100)

        b.add_widget(f)
        b.add_widget(l)
        b.add_widget(btn)
        return b


if __name__ == "__main__":
		mainApp().run()
