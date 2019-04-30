import numpy as np
import matplotlib.pyplot as plt
import random

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
Aroma=[]
listaPer=[]

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

class DataWid(BoxLayout):
    pass

class Experimentos(Screen):
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
        plt.ion() # decimos de forma explícita que sea interactivo
        b=True
        y = [] # los datos que vamos a dibujar y a actualizar
        n=0
        # el bucle infinito que irá dibujando
        while b:
            if n == 90:
                sum=0
                for i in range(0,len(y)):
                    sum=sum+y[i]
                promedio = sum/len(y)
                print(promedio)
                plt.close()
                b=False
            else:
                n = n+1
            #y.append(random.uniform(20, 40)) # añadimos un valor aleatorio a la lista 'y'
            y.append(random.randrange(20, 40, 1))
            # Estas condiciones las he incluido solo para dibujar los últimos 
            # 10 datos de la lista 'y' ya que quiero que en el gráfico se 
            # vea la evolución de los últimos datos
            if len(y) <= 10:
                plt.plot(y)
                plt.xlabel('Tiempo (S)')
                plt.ylabel('Frecuencia')
                plt.ylim(20,40)
                plt.xlim(0,60)
            else:
                plt.plot(y[-60:])
                plt.xlabel('Tiempo (S)')
                plt.ylabel('Frecuencia')
                plt.ylim(20,40)
                plt.xlim(0,60)
            plt.pause(0.05) # esto pausará el gráfico
            plt.cla() # esto limpia la información del axis (el área blanca donde
                    # se pintan las cosas.
        plt.close()

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