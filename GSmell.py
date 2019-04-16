import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

class Pantalla(BoxLayout):
    def mostrar_menu(self):
        menu=MenuPop()
        menu.open()

class Experimentos(Screen):
    pass

class Brain(Screen):
    pass

class Personas(Screen):
    pass

class Aromas(Screen):
    pass

class Sm(ScreenManager):
    pass

class MenuPop(Popup):
    pass

class GSmellApp(App):

    def build(self):
        return Pantalla()

GSmellApp().run()