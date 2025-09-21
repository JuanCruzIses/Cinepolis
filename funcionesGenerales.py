
# Crear funcion buscarPelicula:
#     -Solicitar al usuario que ingrese el nombre de la pelicula
#     -Usar expresiones regulares (debe buscar similitudes por palabra, ejemplo: "el " = "El padrino", "El transportador", "El dia despues de mañana")
# 	    |_Combinar con map y funciones lambda para generar la lista de coincidencias
#         |_Aplicar un bucle for en la lista de coincidencias y que devuelva un listado con selector por números 1,2,3 (ejemplo: Si busca "Harry potter" debería devolver una lista con "Harry potter I", "Harry potter II", "Harry potter III", etc)
#         |_A partir de la eleccion del usuario que retorne el diccionario de la pelicula elegida

from db import listaPeliculas
import re
from Levenshtein import distance

"""
    Funcionamiento general:
    1.Se solicita al usuario que ingrese el nombre de la pelicula a buscar
    2.A partir de un patron de busqueda, se filtra la lista de peliculas buscando coincidencias
    4.Si no se encuentran coincidencias, se aplica una busqueda por similitud usando la distancia de Levenshtein (compara la diferencia existente entre la pelicula a buscar y los titulos de la lista de peliculas)
    3.Si se encuentran coincidencias, se muestran en un listado numerado y a partir de la eleccion del usuario se retorna el diccionario de la pelicula elegida
    5.Si no se encuentran coincidencias, se informa al usuario y se retorna 0

    Informacion complementaria:
    Usamos re.compile para compilar todas las opciones de busqueda
    Usamos re.escape para evitar que caracteres especiales rompan la busqueda
    Usamos re.IGNORECASE para que no diferencie entre mayusculas y minusculas
"""
def buscarPelicula():
    peliculaABuscar = input("Ingrese el nombre de la película a buscar: ").strip().lower()
    while peliculaABuscar == "":
        peliculaABuscar = input("La busqueda no puede estar vacía. Ingrese el nombre de la película a buscar: ").strip().lower()
    patron = re.compile(re.escape(peliculaABuscar), re.IGNORECASE)
    resultados = [p for p in listaPeliculas if patron.search(p["titulo"].lower())]

    if not resultados:
        umbral = 4
        resultados = [p for p in listaPeliculas if distance(peliculaABuscar, p["titulo"].lower()) <= umbral]
    
    
    if resultados:
        print("Resultados encontrados:")
        for i in range(len(resultados)):
            print(f"{i+1}. {resultados[i]['titulo']}")
        print("")
        numeroPeliculaElegida = int(input("Seleccione el número de la película deseada: "))
        while numeroPeliculaElegida < 1 or numeroPeliculaElegida > len(resultados):
            numeroPeliculaElegida = int(input("Número inválido. Seleccione un número de la lista brindada: "))
        seleccionada = resultados[numeroPeliculaElegida - 1]
        print("Película seleccionada:", seleccionada)
        return seleccionada
    
    else:
        print("No se encontraron coincidencias.")
        return 0

