from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.popup import Popup


Builder.load_string(

'''

<Screen1>:
    BoxLayout:
        Button:
            text: root.button_text
            on_release:
                root.popup.open()

<MyPopup>:
    BoxLayout:
        orientation: "vertical"
        Slider:
            on_value:
                root.screen.button_text = str(self.value)
        Button:
            text: "Okey!"
            on_release:
                root.dismiss()

<MySm>:
    Screen1:


'''

)


class MySm(ScreenManager):
    pass


class MyPopup(Popup):

    def __init__(self,screen,**kwargs):
        super(MyPopup,self).__init__(**kwargs)
        self.screen = screen


class Screen1(Screen):
    button_text = StringProperty("text")
    def __init__(self,**kwargs):
        super(Screen1,self).__init__(**kwargs)
        self.popup = MyPopup(self)


class MyApp(App):

    def build(self):
        return MySm()


MyApp().run()