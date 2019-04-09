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
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.popup import Popup
import pymongo
import datetime
from pymongo import MongoClient
client=MongoClient("mongodb+srv://GSmell:gsmellalce1@cluster0-sgq75.mongodb.net/test?retryWrites=true")
db=client.GSmell
evaluados=db.Evaluados

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

    nombre = ObjectProperty(None)
    id_ = ObjectProperty(None)
    edad = ObjectProperty(None)
    sexo = ObjectProperty(None)
    fecha = ObjectProperty(None)
  
    def btn(self):
        show_popup()
          
    def insert(self):

        pacientes={ 
               "nombre":self.nombre.text,
               "sexo":self.sexo.text,
               "edad":self.edad.text,
               "fecha":self.fecha.text,
               "frecuencia":"10",
             }

        evaluados.insert_one(pacientes)

        self.reset()
    
    def reset(self):
        self.nombre.text = ""
        self.sexo.text = ""
        self.edad.text = ""
        self.fecha.text = ""



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