import pymongo
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from pymongo import MongoClient


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass
    def btn(self):
        show_popup()


class WindowManager(ScreenManager):
    pass

class Pop(FloatLayout):
    pass


kv = Builder.load_file("App.kv")


class GSmellApp(App):
    def build(self):
        return kv

def show_popup():
    show = Pop()

    popupWindow = Popup(title= "Agregar Paciente", content = show, size_hint=(None, None), size = (400,400))

    popupWindow.open()


if __name__=="__main__":
    GSmellApp().run()