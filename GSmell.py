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
from kivy.uix.listview import ListItemButton
from kivy.adapters.listadapter import ListAdapter
from pymongo import MongoClient

Window.clearcolor= (0.5, 0.5, 0.5, 1)

client=MongoClient('mongodb+srv://GSmell:gsmellalce1@cluster0-sgq75.mongodb.net/test?retryWrites=true')
db=client.GSmell
evaluadosDB=db.Evaluados
usuariosDB=db.Usuarios
experimentosDB = db.Experimentos
personasDB = db.Personas
aromasDB = db.Aromas
Aroma=[]
listaAr=[]
listaPer=[]
listaNomPer=[]
for doc in personasDB.find():
    listaNomPer.append(doc["Nombre"])
listaNomExp=[]
for doc in experimentosDB.find():
    listaNomExp.append(doc["Nombre"])
listaNomAr=[]
for doc in aromasDB.find():
    listaNomAr.append(doc["Nombre"])



class listadebotones(ListItemButton):
    pass

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

class Experimentos(Screen):
    def crear_exp(self):
        exp = ExperimentoPop()
        exp.open()

    def actualizar_lista(self):
        listaNomExp.clear()
        for doc in experimentosDB.find():
            listaNomExp.append(doc["Nombre"])
        self.ids.ListaExpp.adapter.data=listaNomExp
        self.ids.ListaExpp._trigger_reset_populate()
        print("Lista de experimentos actualizada")
        
class ExperimentoPop(Popup):

    def listPer(self, values):
        promedio = 0
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
            y.append(random.uniform(20, 40))
            # añadimos un valor aleatorio a la lista 'y'
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
            #con esto se guarda la grafica, se debe reemplazar la ubicacion:
            plt.savefig('/Users/JLH/Desktop/Resultado.png', transparent=False)
            plt.cla() # esto limpia la información del axis (el área blanca donde
                    # se pintan las cosas.
        plt.close()
        listaPer.append([values, promedio])
      
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
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].children[0].actualizar_lista()

    def confirmar_exp(self):
        confirmarExp = confirmarExpPop()
        confirmarExp.open()

    def verResultadosExp(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Resultados'
        self.dismiss()

class confirmarExpPop(Popup):
    pass

class Resultados(Screen):
    pass

class Brain(Screen):
    pass

class Personas(Screen):
    def crearPer(self):
        per = personasPopUp()
        per.open()
    
    def actualizar_lista(self):
        listaNomPer.clear()
        for doc in personasDB.find():
            listaNomPer.append(doc["Nombre"])
        self.ids.ListaPerr.adapter.data=listaNomPer
        self.ids.ListaPerr._trigger_reset_populate()
        print("Lista de personas actualizada")

class personasPopUp(Popup):
    def evaluarImagen(self):
        num=int(list(self.ids.imgenCP.background_normal)[9])
        if num==0:
            slv=Popup(title="", separator_height=0, size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y': .5})
            slv.add_widget(Label(text="Todas las imágenes han sido evaluadas"))
            slv.open()
        else:
            if num==5:
                num=0
                self.ids.imgenCP.background_normal='Imagenes/'+str(num)+'.jpg'
            else:
                if num<5:
                    num=num+1
                    self.ids.imgenCP.background_normal='Imagenes/'+str(num)+'.jpg'
        
        

    def crearPer(self):
        new_per={
            "Id": self.ids.inputIdP.text,
            "Nombre": self.ids.inputNombreP.text,
            "Edad": self.ids.inputEdadP.text,
            "Genero": self.ids.inputGeneroP.text
        }
        personasDB.insert_one(new_per)
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].children[0].actualizar_lista()
    def confirmarPersona(self):
        confirmarPer = confirmarPerPop()
        confirmarPer.open()

class confirmarPerPop(Popup):
    pass

class Imagenes(Screen):
    def mostrar(self, btns):
        img=Popup(size_hint=(.6, 0.6), pos_hint={'x': 0.2, 'top': 0.75}, title="", separator_height=0)
        bl=BoxLayout()
        bl.add_widget(Button(background_normal=btns.background_normal))
        img.add_widget(bl)
        img.open()

class AromasPopUp(Popup):
    def crearAr(self):
        new_Ar={
            "Nombre": self.ids.inputNombreA.text,
        }
        aromasDB.insert_one(new_Ar)
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].children[0].actualizar_lista()
    def confirmarAroma(self):
        confirmarAr = confirmarArPop()
        confirmarAr.open()

class confirmarArPop(Popup):
    pass

class Sm(ScreenManager):
    pass

class Ssm(ScreenManager):
    pass
    
class MenuPop(Popup):
    def salir(self):
        megaroot=App.get_running_app()
        megaroot.root.current='LoginScreen'
        self.dismiss()

    def pasar_a_experimentos(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Experimentos'
        MenuPop.dismiss(self)

    def pasar_a_personas(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Personas'
        MenuPop.dismiss(self)

    def pasar_a_aromas(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Imagenes'
        MenuPop.dismiss(self)

    def ocultar_menu(self):
        self.dismiss()

class GSmellApp(App):
    title="GSmell"
    def build(self):
        global rooter
        rooter=Ssm()
        return rooter

    

if __name__=="__main__":
    GSmellApp().run()