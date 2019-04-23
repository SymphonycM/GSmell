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

class LoginScreen(Screen):
    def validar_login(self):
        usr=self.ids.inputCorreoL.text
        contr=self.ids.inputContrasenaL.text
        registrados=usuariosDB.find({"correo":usr , "contraseña":contr})
        if(len(list(registrados))>0):
            self.manager.current='PantallaScreen'
            self.ids.loginIncorrectoLabel.text=""
            self.ids.inputCorreoL.text=""
            self.ids.inputContrasenaL.text=""
        else:
            self.ids.loginIncorrectoLabel.text="Correo o contraseña incorrecto"
            self.ids.inputCorreoL.text=""
            self.ids.inputContrasenaL.text=""

class RegisterScreen(Screen):
    def registrar(self):
        new_usr={
            "correo": self.ids.inputCorreo.text,
            "contraseña": self.ids.inputContrasena.text
        }
        usuariosDB.insert_one(new_usr)

class PantallaScreen(Screen):
    def mostrar_menu(self):
        menu=MenuPop()
        menu.open()
    
class Experimentos(Screen):
    def crear_exp(self):
        exp = ExperimentoPop()
        exp.open()
    def check_memory(self):
        for i in experimentosDB:
            r1 = 'Nombre empresa: '+ i[1]
            r2 = 'Nombre experimento' + i[2]
            r3 = 'Personas: '+ i[3]
            r4 = 'Aromas: '+ i[4]

class ExperimentoPop(Popup):
    def anadir_personas_exp(self):
        anadirPersonas = AnadirPersonasExpPop()
        anadirPersonas.open()
    def anadir_aromas_exp(self):
        anadirAromas = AnadirAromasExpPop()
        anadirAromas.open()
    def registrarExp(self):
        listaPer= ["Jorge", "Samuel", "Esteban"]
        listaAr= ["Aroma 1", "Aroma 2"]
        new_exp={
            "Empresa": self.ids.inputEmpresaL.text,
            "Nombre": self.ids.inputNombreL.text,
            "Personas": listaPer,
            "Aromas": listaAr
        }
        experimentosDB.insert_one(new_exp)
    def confirmar_exp(self):
        confirmarExp = confirmarExpPop()
        confirmarExp.open()
class AnadirPersonasExpPop(Popup):
    def btn_chk(self):
        #ListaPersonasExp = []
        #ListaPersonasExp.append(self.ids.self.text)
        pass

class AnadirAromasExpPop(Popup):
    def btn_chk(self):
        pass

class confirmarExpPop(Popup):
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