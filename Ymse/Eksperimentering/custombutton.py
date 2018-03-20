# custombutton.py

from kivy.app import App
from kivy.uix.widget import Widget


class MyWidget(Widget):
    pass


class CustomButtonApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    CustomButtonApp().run()