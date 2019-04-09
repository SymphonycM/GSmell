###### Único código general
import pymongo
import datetime
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://GSmell:queremosplata@cluster0-sij7n.mongodb.net/test?retryWrites=true")
db=client.GSmell
evaluados=db.Evaluados






# db=client.GSmell
# evaluados=db.Evaluados
###### Crear una base de datos en Mongo llamada "GSmell", dentro de ella, una colección llamada "Evaluados" (con las mayúsculas)


###### Este bloque guarda un documento nuevo en la base de datos, se pueden cambiar los datos del lado derecho, con las comillas, por variables 

# insert={ 
#     "nombre":"Juliana",
#     "sexo":"Mujer",
#     "edad":"30",
#     "fecha":"08/04/2017",
#     "pestres":"10",
#     "prel":"70",
#     "potro":"20"
# }
# evaluados.insert_one(insert)



######Insertar más de un paciente a la vez, para insertar más, copiar y pegar un bloque de llave y editar información

# insert={
#     "nombre":"Andrea",
#     "sexo":"Mujer",
#     "edad":"24",
#     "fecha":"08/04/2017",
#     "pestres":"35",
#     "prel":"45",
#     "potro":"20"
# },{
#     "nombre":"Miguel",
#     "sexo":"Hombre",
#     "edad":"24",
#     "fecha":"05/03/2018",
#     "pestres":"10",
#     "prel":"90",
#     "potro":"10"
# }
# evaluados.insert_many(insert)


###### Aquí guarda todos los documentos en una lista llamada "lista", cada posición es otra lista en la que está la información de cada paciente
###### La lista de cada paciente está en el orden: nombre, sexo, edad, fecha, porcentaje de estrés, porc. de relajación, porc. de otro.

numero=evaluados.distinct("_id")
evlas=evaluados.find()
lista=[[]for x in range(0, len(numero))]
cont=0
for i in evlas:
    lista[cont]=[i["nombre"],i["sexo"],i["edad"],i["fecha"],i["pestres"],i["prel"],i["potro"]]
    cont=cont+1
print(lista)



###### Filtro de búsqueda por un sólo parámetro, se puede cambiar "sexo" y "mujer" por la variable y el valor a buscar, siempre dentro de
###### llaves, se guarda en una lista llamada "lista" donde cada posición es otra lista con la información de cada paciente, en el orden:
###### nombre, sexo, edad, fecha, porcentaje de estrés, porc. de relajación, porc. de otro.

# numero=evaluados.find({"sexo":"Mujer"}).distinct("_id")
# evlas=evaluados.find({"sexo":"Mujer"})
# lista=[[]for x in range(0, len(numero))]
# cont=0
# for i in evlas:
#     lista[cont]=[i["nombre"],i["sexo"],i["edad"],i["fecha"],i["pestres"],i["prel"],i["potro"]]
#     cont=cont+1
# print(lista)