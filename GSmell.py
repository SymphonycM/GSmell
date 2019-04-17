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

Window.clearcolor= (0.5, 0.5, 0.5, 1)

class LoginScreen(Screen):
    pass

class PantallaScreen(Screen):
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

class Ssm(ScreenManager):
    pass
    
class MenuPop(Popup):
    def pasar_a_experimentos(self):
        pass
    
    def ocultar_menu(self):
        self.dismiss()

class GSmellApp(App):
    
    def build(self):
        return Ssm()

GSmellApp().run()