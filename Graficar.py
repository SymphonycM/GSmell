import matplotlib.pyplot as plt
import numpy as np
#Variables
def main():
    numUsuario = int(input("Numero de usuarios: "))
    datos = []
    nom = []
    comentario = " "
    estresado = 0
    relajado= 0
    concentrado = 0

    for i in range(numUsuario):
        nombre = input("Nombre del usuario: ")
        frecuencia = float(input("Frecuancia del usuario: "))
        nom.append(nombre) 
        datos.append(frecuencia)
        if numUsuario == 1:
            comentario = input("Comentarios: ")
        else:
            comentario = " "
    if numUsuario == 1:
        graficoUnaBarra(datos, nom, comentario, estresado, relajado, concentrado, numUsuario)
    else:
        graficoDeBarras(datos, nom, numUsuario, estresado, relajado, concentrado)

def graficoUnaBarra(datos, nom, comentario, estresado, relajado, concentrado, numUsuario):
    x = range(len(datos))
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(211)
    ax.bar(x, datos, width=0.8, align='center')
    plt.ylim(3,50)
    ax.set_xticks(x)
    ax.set_xticklabels(nom)
    plt.text(0,-25, comentario, fontsize = 10, horizontalalignment='center', verticalalignment='center')
    definir(numUsuario, datos, estresado, relajado, concentrado)
    plt.show()

def graficoDeBarras(datos, nom, numUsuario, estresado, relajado, concentrado):
    x = range(len(datos))
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(211) 
    ax.bar(x, datos, width=0.5, align='center')
    plt.ylim(3,50)
    ax.set_xticks(x)
    ax.set_xticklabels(nom, rotation = 90)
    definir(numUsuario, datos, estresado, relajado, concentrado)
    
def definir(numUsuario, datos, estresado, relajado, concentrado):
    a = np.arange(numUsuario)
    for x, y in zip(a, datos):
        if datos[x] >= 3 and datos[x] < 8:
            plt.text(x + 0.01, y+0.5, 'Estresado', horizontalalignment= 'center', verticalalignment='bottom', fontsize=10, rotation=90, color='dimgrey')
            estresado = estresado+1
        if datos[x] >= 8 and datos[x] < 12:
            plt.text(x + 0.01, y+0.5, 'Relajado', horizontalalignment= 'center', verticalalignment='bottom', fontsize=10, rotation=90, color='dimgrey')
            relajado =relajado + 1
        if datos[x] >= 12 and datos[x] < 33:
            plt.text(x + 0.01, y+0.5, 'Concentrado', horizontalalignment= 'center', verticalalignment='bottom', fontsize=10, rotation=90, color='dimgrey')
            concentrado =concentrado + 1
    if numUsuario > 1:
        graficoCircular(estresado, relajado, concentrado, numUsuario)

def graficoCircular(estresado, relajado, concentrado, numUsuario):
    total = estresado+relajado+concentrado
    estres = estresado * 100 / total
    relax = relajado * 100 / total
    concentracion = concentrado * 100 /total
    fig = plt.figure(u'Diagrama circular')
    labels = 'Estres', 'Concentración', 'Relajado'
    sizes = [estres, concentracion, relax]
    colors = ['lightcoral', 'gold', 'lightskyblue', '']
    explode = (0, 0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=130)
    plt.axis('equal')
    plt.show()

main()