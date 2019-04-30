import kivy
import pymongo
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
from pymongo import MongoClient

Window.clearcolor= (0.5, 0.5, 0.5, 1)
client=MongoClient('mongodb+srv://GSmell:gsmellalce1@cluster0-sgq75.mongodb.net/test?retryWrites=true')
db=client.GSmell
evaluadosDB=db.Evaluados
usuariosDB=db.Usuarios
experimentosDB = db.Experimentos
personasDB = db.Personas
Aroma=[]
listaPer=[]

class LoginScreen(Screen):
    def validar_login(self):
        usr=self.ids.inputCorreoL.text
        contr=self.ids.inputContrasenaL.text
        registrados=usuariosDB.find({"correo":usr , "contrasena":contr})
        if(len(list(registrados))>0):
            self.manager.current='PantallaScreen'
            self.ids.loginIncorrectoLabel.text=""
            self.ids.inputCorreoL.text=""
            self.ids.inputContrasenaL.text=""
        else:
            self.ids.loginIncorrectoLabel.text="Correo o contrasena incorrecto"
            self.ids.inputCorreoL.text=""
            self.ids.inputContrasenaL.text=""

class RegisterScreen(Screen):
    def registrar(self):
        new_usr={
            "correo": self.ids.inputCorreo.text,
            "contrasena": self.ids.inputContrasena.text
        }
        usuariosDB.insert_one(new_usr)

class PantallaScreen(Screen):
    def mostrar_menu(self):
        menu=MenuPop()
        menu.open()

class DataWid(BoxLayout):
    pass

class Experimentos(Screen):
    def check_memory(self):
        for doc in experimentosDB.find():
            r1 = "Empresa: "+doc["Empresa"]+ "\n"
            r2 = "Nombre: " +doc["Nombre"]+ "\n"
            r3 = "Personas: " + ", ".join(doc["Personas"])+ "\n"
            r4 = "Aroma: " + "".join(doc["Aromas"])+ "\n"
            print(r1+r2+r3+r4)
    def crear_exp(self):
        exp = ExperimentoPop()
        exp.open()
class ExperimentoPop(Popup):
    def listPer(self, values):
        listaPer.append(values)
    def listAr(self, value):
        Aroma.append(value)
    def registrarExp(self):
        new_exp={
            "Empresa": self.ids.inputEmpresaL.text,
            "Nombre": self.ids.inputNombreL.text,
            "Personas": listaPer,
            "Aromas": Aroma
        }
        experimentosDB.insert_one(new_exp)
    def confirmar_exp(self):
        confirmarExp = confirmarExpPop()
        confirmarExp.open()

class confirmarExpPop(Popup):
    pass

class Brain(Screen):
    pass

#Todo lo relacionado a personas y sus popups:
class Personas(Screen):
    def crearPer(self):
        per = personasPopUp()
        per.open()
    
    def verListaPer(self):
        pass
        
class personasPopUp(Popup):
    def crearPer(self):
        new_per={
            "Id": self.ids.inputIdP.text,
            "Nombre": self.ids.inputNombreP.text,
            "Edad": self.ids.inputEdadP.text,
            "Genero": self.ids.inputGeneroP.text
        }
        personasDB.insert_one(new_per)
    def confirmarPersona(self):
        confirmarPer = confirmarPerPop()
        confirmarPer.open()

class confirmarPerPop(Popup):
    pass

#------------------------------------------------------------------------------------------------------------------
class Aromas(Screen):
    pass

class Sm(ScreenManager):
    pass

class Ssm(ScreenManager):
    pass
    
class MenuPop(Popup):
    def pasar_a_experimentos(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Experimentos'
        MenuPop.dismiss(self)

    def pasar_a_personas(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Personas'

    def pasar_a_aromas(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Aromas'

    def ocultar_menu(self):
        self.dismiss()

class GSmellApp(App):
    
    def build(self):
        global rooter
        rooter=Ssm()
        return rooter

GSmellApp().run()