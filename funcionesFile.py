import os
import json
from db import listaPeliculas, listaResenas, listaUsuarios

rutaRaiz = os.path.dirname(__file__)

def traerJson(nombreArchivo):
    file = os.path.join(rutaRaiz, nombreArchivo)
    try:
        with open(file, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except Exception as e:
        return(f'Error: {e}')

# Funcion creada para realizar el pasaje a formato JSON
#La funcion es dinamica ya que recibe como parametros el nombre del archivo que se desea crear y el objeto python que se desea escribir en el archivo JSON
#Se utiliza "ensure_ascii=False" para evitar que los textos que llevan tildes sean escapados al transcribir de un formato a otro
#Se realiza manejo de errores para prevenir que el programa "rompa" en caso de algun error en la creacion/escritura del archivo json
def convertirJson(nombreArchivo, dbPython):
    fileJSON = os.path.join(rutaRaiz, nombreArchivo)

    try:
        with open(fileJSON, "w", encoding='utf-8') as file:
            json.dump(dbPython, file, indent=4, ensure_ascii=False)
            print(f'Se realizo de forma correcta la migracion a {nombreArchivo}')
    except Exception as e:
        print(f'Fallo la migracion a {nombreArchivo}')

# ---- Ejecuciones utilizadas para realizar el traspaso de las listas de diccionarios utilizados como DB originalmente, a formato JSON
# convertirJson("peliculas.json", listaPeliculas)
# convertirJson("resenas.json", listaResenas)
# convertirJson("usuarios.json", listaUsuarios)