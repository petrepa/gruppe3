#definerer at vi skal bruke kivy
import kivy
import random

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
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView

#Funksjonane til framskjerm og menyen
class FrontScreen(Screen):
	pass

class MainWidget(Screen):
	pass


#Funksjonane til dei ulike modulane
class KlimaScreen(Screen):
	pass
	

class HistorieScreen(Screen):
	pass

class SeverdigScreen(Screen):
	pass

class Veibeskrivelser(Screen):
	pass


class Museum(Screen):
	pass

class Rockheim(Screen):
	pass
class RockheimInfo(Screen):
	pass

class TrondelagFolkemuseum(Screen):
	pass
class TrondelagFolkemuseumInfo(Screen):
    pass

class RingveMuseum(Screen):
	pass
class RingveMuseumInfo(Screen):
    pass

class Vitenskapsmuseet(Screen):
	pass
class VitenskapsmuseetInfo(Screen):
    pass

class Rustkammeret(Screen):
	pass
class RustkammeretInfo(Screen):
    pass

class NordenfjeldskeKunst(Screen):
	pass
class NordenfjeldskeKunstInfo(Screen):
	pass

class NorskeDovemuseum(Screen):
	pass
class NorskDovemuseumInfo(Screen):
	pass

class TrondheimKunstmuseum(Screen):
	pass
class TrondheimKunstmuseumInfo(Screen):
	pass

class JodiskeMuseum(Screen):
	pass
class JodiskMuseumInfo(Screen):
	pass

class TrondheimSjofartsmuseum(Screen):
	pass
class TrondheimSjofartsmuseumInfo(Screen):
	pass




class HistoriskeSteder(Screen):
	pass

class Nidarosdomen(Screen):
	pass
class NidarosdomenInfo(Screen):
	pass

class Stiftsgarden(Screen):
	pass
class StiftsgardenInfo(Screen):
	pass

class GamleBybro(Screen):
	pass
class GamleBybroInfo(Screen):
	pass

class KristianstenFestning(Screen):
	pass
class KristianstenFestningInfo(Screen):
	pass

class Erkebispegarden(Screen):
	pass
class ErkebispegardenInfo(Screen):
	pass

class Munkholmen(Screen):
	pass
class MunkholmenInfo(Screen):
	pass

class Bakklandet(Screen):
	pass
class BakklandetInfo(Screen):
	pass

class VarFrueKirke(Screen):
	pass
class VarFrueKirkeInfo(Screen):
	pass



class Kultur(Screen):
	pass

class Vitensenteret(Screen):
	pass
class VitensenteretInfo(Screen):
	pass

class KunsthallTrondheim(Screen):
	pass
class KunsthallTrondheimInfo(Screen):
	pass

class LitteraturhusetTrondheim(Screen):
	pass
class LitteraturhusetTrondheimInfo(Screen):
	pass

class KultursenteretISAK(Screen):
	pass
class KultursenteretISAKInfo(Screen):
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


class SelectionScreen(Screen):
    testScreen = StringProperty('Screen1')

    checbox_is_active = ObjectProperty(False)
    serverdigheter = []
    museum = 0
    historisk = 0
    kultur = 0
    natur = 0
    mat = 0
    aktiviteter = 0

    def checkbox_museum_cliked(self, instance, value):
        if value is True:
            print("Checkbox 1 Checked")
            self.museum = 1
        else:
            print("Checkbox 1 is Unchecked")
            self.museum = 0
    def checkbox_historisk_cliked(self, instance, value):
        if value is True:
            print("Checkbox 2 Checked")
            self.historisk = 1
        else:
            print("Checkbox 2 is Unchecked")
            self.historisk = 0
    def checkbox_kultur_cliked(self, instance, value):
        if value is True:
            print("Checkbox 3 Checked")
            self.kultur = 1
        else:
            print("Checkbox 3 is Unchecked")
            self.kultur = 0
    def checkbox_natur_cliked(self, instance, value):
        if value is True:
            print("Checkbox 4 Checked")
            self.natur = 1
        else:
            print("Checkbox 4 is Unchecked")
            self.natur = 0
    def checkbox_mat_cliked(self, instance, value):
        if value is True:
            print("Checkbox 5 Checked")
            self.mat = 1
        else:
            print("Checkbox 5 is Unchecked")
            self.mat = 0
    def checkbox_aktiviteter_cliked(self, instance, value):
        if value is True:
            print("Checkbox 6 Checked")
            self.aktiviteter = 1
        else:
            print("Checkbox 6 is Unchecked")
            self.aktiviteter = 0

    def screenSelector(self):
        liste_mu = ['rockheiminfo', 'trondelagfolkemuseuminfo',
                    'ringvemuseuminfo', 'vitenskapsmuseetinfo',
                    'rustkammeretinfo', 'nordenfjeldskekunstinfo',
                    'norskdovemuseuminfo', 'trondheimkunstmuseuminfo',
                    'jodiskmuseuminfo', 'trondheimsjofartsmuseuminfo']
        liste_h = ['nidarosdomeninfo', 'stiftsgardeninfo',
                   'gamlebybroinfo', 'kristianstenfestninginfo',
                   'erkebispegardeninfo', 'munkholmeninfo',
                   'bakklandetinfo', 'varfruekirkeinfo']
        liste_k = ['vitensenteretinfo', 'kunsthalltrondheiminfo',
                   'litteraturhusettrondheiminfo', 'kultursenteretISAKinfo']
        liste_n = ['burmaklippen', 'geitfjellet',
                   'vattakammen', 'ladestien']
        liste_ma = ['tyholttarnet', 'ilaBrannstasjon',
                    'antikvariatet', 'arvesolvetFolkekafe',
                    'cafeNim', 'cafeNiMuser',
                    'rosenborgDampbakeri', 'sellenraaBokBar',
                    'trondheimMikrobryggeri', 'cafeLokka',
                    'bakklandetSkydsstasjon']
        liste_a = ['klatresenter', 'turnhall',
                   'bowling', 'trampolinepark',
                   'gokartOgLazerx', 'escapeReality']
        antallSkjermer = 43

        if int(self.museum) == 1:
            self.serverdigheter.extend(liste_mu)
            print("Museum i liste")
        if int(self.historisk) == 1:
            self.serverdigheter.extend(liste_h)
            print("Historisk i liste")
        if int(self.kultur) == 1:
            self.serverdigheter.extend(liste_k)
            print("Kultur i liste")
        if int(self.natur) == 1:
            self.serverdigheter.extend(liste_n)
            print("Natur i liste")
        if int(self.mat) == 1:
            self.serverdigheter.extend(liste_ma)
            print("Mat i liste")
        if int(self.aktiviteter) == 1:
            self.serverdigheter.extend(liste_a)
            print("Aktiviteter i liste")

        if not self.serverdigheter:
            number = random.randint(0, antallSkjermer)
            self.serverdigheter.extend(liste_mu)
            self.serverdigheter.extend(liste_h)
            self.serverdigheter.extend(liste_k)
            self.serverdigheter.extend(liste_n)
            self.serverdigheter.extend(liste_ma)
            self.serverdigheter.extend(liste_a)
        else:
            number = random.randint(0, len(self.serverdigheter))

        self.testScreen = self.serverdigheter[number]
        return self.testScreen


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
