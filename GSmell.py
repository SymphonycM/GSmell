import numpy as np
import matplotlib.pyplot as plt
import random
import kivy
import pymongo
import graf as graficas
import os
import time
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
from matplotlib import pyplot
color = 1, 1, 1,1
Window.clearcolor=(color)

client=MongoClient('mongodb+srv://GSmell:gsmellalce1@cluster0-sgq75.mongodb.net/test?retryWrites=true')
db=client.GSmell
evaluadosDB=db.Evaluados
usuariosDB=db.Usuarios
experimentosDB = db.Experimentos
personasDB = db.Personas
listaPer=[]
listaNomPer=[]
listaGenPer=[]
listaEdadPer=[]
IlusionLikes=[]
listaLikes=[]
listaGeneros=[]
arrayLike=[]


for doc in personasDB.find():
    listaNomPer.append(doc["Nombre"])

for doc in personasDB.find():
    listaEdadPer.append(doc["Edad"])

for doc in personasDB.find():
    listaGenPer.append(doc["Genero"])

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

class Resultados(Screen):
    pass

class Brain(Screen):
    pass

class Estadisticas(Screen):
    def actualizar(self):
        dove = 0
        iphone = 0
        mcdonalds = 0
        coca = 0
        yogurt = 0
        for doc in personasDB.find():
            arrayLike = doc["Likes"]
            for i in range(len(arrayLike)):
                if i==0 and arrayLike[i] == 'Like': dove= dove+1
                if i==1 and arrayLike[i] == 'Like': iphone = iphone + 1
                if i==2 and arrayLike[i] == 'Like': mcdonalds= mcdonalds+1
                if i==3 and arrayLike[i] == 'Like': coca = coca+1
                if i==4 and arrayLike[i] == 'Like': yogurt = yogurt+1
        labels = 'Like', 'Dislike'
        sizes = [dove, len(listaNomPer) - dove]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Dove')
        plt.savefig("Graficas/fig0.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [iphone, len(listaNomPer) - iphone]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca iPhone')
        plt.savefig("Graficas/fig1.png")
        plt.close()    
            
        labels = 'Like', 'Dislike'
        sizes = [mcdonalds, len(listaNomPer) - mcdonalds]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u"Marca McDonald's")
        plt.savefig("Graficas/fig2.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [coca, len(listaNomPer) - coca]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Caca-Cola')
        plt.savefig("Graficas/fig3.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [yogurt, len(listaNomPer) - yogurt]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Yogurt')
        plt.savefig("Graficas/fig4.png")
        plt.close()
    def drop_down_list_gen(self, value):
        generoPer = personasDB.find({"Genero": value})
        contador = 0
        dove = 0
        iphone = 0
        mcdonalds = 0
        coca = 0
        yogurt = 0
        for doc in generoPer:
            print(doc)
            contador = contador+1
            arrayLike = doc["Likes"]
            for i in range(len(arrayLike)):
                if i==0 and arrayLike[i] == 'Like': dove= dove+1
                if i==1 and arrayLike[i] == 'Like': iphone = iphone + 1
                if i==2 and arrayLike[i] == 'Like': mcdonalds= mcdonalds+1
                if i==3 and arrayLike[i] == 'Like': coca = coca+1
                if i==4 and arrayLike[i] == 'Like': yogurt = yogurt+1
        labels = 'Like', 'Dislike'
        sizes = [dove, contador - dove]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Dove')
        plt.savefig("Graficas/fig0.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [iphone, contador - iphone]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca iPhone')
        plt.savefig("Graficas/fig1.png")
        plt.close()    
            
        labels = 'Like', 'Dislike'
        sizes = [mcdonalds, contador - mcdonalds]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u"Marca McDonald's")
        plt.savefig("Graficas/fig2.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [coca, contador - coca]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Caca-Cola')
        plt.savefig("Graficas/fig3.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [yogurt, contador - yogurt]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Yogurt')
        plt.savefig("Graficas/fig4.png")
        plt.close()
    def drop_down_list_ran(self, value):
        personas = []
        edad = int(value[0:2])
        edad1 = int(value[3:5])
        print(edad)
        contador = 0
        dove = 0
        iphone = 0
        mcdonalds = 0
        coca = 0
        yogurt = 0
        for doc in personasDB.find():
            com = int(doc["Edad"])
            if com >= edad and com <= edad1:
                personas.append(doc)
                contador = contador+1
        print(personas)
        for x in personas:
            arrayLike = x["Likes"]
            for i in range(len(arrayLike)):
                if i==0 and arrayLike[i] == 'Like': dove= dove+1
                if i==1 and arrayLike[i] == 'Like': iphone = iphone + 1
                if i==2 and arrayLike[i] == 'Like': mcdonalds= mcdonalds+1
                if i==3 and arrayLike[i] == 'Like': coca = coca+1
                if i==4 and arrayLike[i] == 'Like': yogurt = yogurt+1
        labels = 'Like', 'Dislike'
        sizes = [dove, contador - dove]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Dove')
        plt.savefig("Graficas/fig0.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [iphone, contador - iphone]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca iPhone')
        plt.savefig("Graficas/fig1.png")
        plt.close()    
            
        labels = 'Like', 'Dislike'
        sizes = [mcdonalds, contador - mcdonalds]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u"Marca McDonald's")
        plt.savefig("Graficas/fig2.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [coca, contador - coca]
        colors = ['lightcoral', 'gold']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Caca-Cola')
        plt.savefig("Graficas/fig3.png")
        plt.close()

        labels = 'Like', 'Dislike'
        sizes = [yogurt, contador - yogurt]
        colors = ['blue', 'orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=130)
        plt.axis('equal')
        plt.title(u'Marca Yogurt')
        plt.savefig("Graficas/fig4.png")
        plt.close()
    def mostrar(self, btns):
        img=Popup(size_hint=(.6, 0.6), pos_hint={'x': 0.2, 'top': 0.75}, title="", separator_height=0)
        bl=BoxLayout()
        bl.add_widget(Button(background_normal=btns.background_normal))
        img.add_widget(bl)
        img.open()
        
estadis = Estadisticas()
estadis.actualizar()

class Personas(Screen):
    def ver(self, nom):
        nlikes=0
        persona=[]
        likesitos=[]
        tipo=personasDB.find({"Nombre":nom})
        for x in tipo:
            persona.append(x["Id"])
            persona.append(x["Nombre"])
            persona.append(x["Edad"])
            persona.append(x["Genero"])
            likesitos=x["Likes"]
        for n in likesitos:
            if n=="Like":
                nlikes=nlikes+1
        labels="like", "Dislike"
        plt.pie([nlikes, len(likesitos)-nlikes], labels=labels, autopct='%1.1f%%', shadow=True, startangle=130)
        plt.savefig("mostranding.png")
        plt.close()
        img=Popup(size_hint=(.6, .6), pos_hint={'x': 0.2, 'top': 0.85}, title="", separator_height=0)
        bl=BoxLayout(orientation='vertical', space=5)
        bl.add_widget(Label(text="Id:"+persona[0], size_hint=(1, .05), halign='left'))
        bl.add_widget(Label(text="Nombre:"+persona[1], size_hint=(1, .05), halign='left'))
        bl.add_widget(Label(text="Edad:"+persona[2], size_hint=(1, .05), halign='left'))
        bl.add_widget(Label(text="Genero:"+persona[3], size_hint=(1, .05), halign='left'))
        bl2=BoxLayout(orientation='horizontal', cols=2)
        bl2.add_widget(Label(text="Resultados por imagenes:\n1: "+likesitos[0]+"\n2: "+likesitos[1]+"\n3: "+likesitos[2]+"\n4: "+likesitos[3]+"\n5: "+likesitos[4]))
        botoncito1=Button(background_normal='mostranding.jpg', size_hint=(1, .7))
        bl2.add_widget(botoncito1)
        bl.add_widget(bl2)
        img.add_widget(bl)
        img.open()

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
    
    def limpiarDatos(self):
        personasDB.delete_many({})
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].children[0].actualizar_lista()
        slv=Popup(title="", separator_height=0, size_hint=(.4, .1), pos_hint={'center_x': .5, 'center_y': .5})
        slv.add_widget(Label(text="Datos borrados"))
        slv.open()

class personasPopUp(Popup):
    def evaluarImagen(self):
        num=int(list(self.ids.imgenCP.background_normal)[9])
        persona=len(list(personasDB.find()))+1
        if num==0:
            slv=Popup(title="", separator_height=0, size_hint=(.4, .1), pos_hint={'center_x': .5, 'center_y': .5})
            slv.add_widget(Label(text="Todas las imágenes han sido evaluadas"))
            slv.open()
        else:
            if num==5:
                graficas.leer('DatosExperimentos/Persona'+str(persona)+'/'+str(num)+'.1.txt')
                f=open('DatosExperimentos/Persona'+str(persona)+'/'+str(num)+'.2.lab')
                IlusionLikes.append(f.read())
                num=0
                self.ids.imgenCP.background_normal='Imagenes/'+str(num)+'.jpg'
            else:
                if num<5:
                    graficas.leer('DatosExperimentos/Persona'+str(persona)+'/'+str(num)+'.1.txt')
                    f=open('DatosExperimentos/Persona'+str(persona)+'/'+str(num)+'.2.lab')
                    IlusionLikes.append(f.read())
                    num=num+1
                    print(persona)
                    self.ids.imgenCP.background_normal='Imagenes/'+str(num)+'.jpg'
        

    def crearPer(self):
        num=int(list(self.ids.imgenCP.background_normal)[9])
        if num==0:
            new_per={
                "Id": self.ids.inputIdP.text,
                "Nombre": self.ids.inputNombreP.text,
                "Edad": self.ids.inputEdadP.text,
                "Genero": self.ids.spinnerIdGenero.text,
                "Likes": IlusionLikes
            }
            print(IlusionLikes)
            personasDB.insert_one(new_per)
            IlusionLikes.clear()
            megaroot=App.get_running_app()
            megaroot.root.children[0].children[0].children[0].children[0].actualizar_lista()
            self.dismiss()
            confirmarPer = confirmarPerPop()
            confirmarPer.open() 
        else:
            slv=Popup(title="", separator_height=0, size_hint=(.4, .1), pos_hint={'center_x': .5, 'center_y': .5})
            slv.add_widget(Label(text="Faltan imágenes por evaluar"))
            slv.open()

    def clear(self):
        IlusionLikes.clear()
        print("Limpia")

class confirmarPerPop(Popup):
    pass

class Imagenes(Screen):
    def mostrar(self, btns):
        img=Popup(size_hint=(.6, 0.6), pos_hint={'x': 0.2, 'top': 0.75}, title="", separator_height=0)
        bl=BoxLayout()
        bl.add_widget(Button(background_normal=btns.background_normal))
        img.add_widget(bl)
        img.open()

class Sm(ScreenManager):
    pass

class Ssm(ScreenManager):
    pass
    
class MenuPop(Popup):
    def salir(self):
        megaroot=App.get_running_app()
        megaroot.root.current='LoginScreen'
        self.dismiss()

    def pasar_a_estadisticas(self):
        megaroot=App.get_running_app()
        megaroot.root.children[0].children[0].children[0].current='Estadisticas'
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