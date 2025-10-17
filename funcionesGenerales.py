from db import listaPeliculas
import re

"""
    Funcionamiento general:
    1.Se solicita al usuario que ingrese el nombre de la pelicula a buscar
    2.A partir de un patron de busqueda, se filtra la lista de peliculas buscando coincidencias
    3.Si se encuentran coincidencias, se muestran en un listado numerado y a partir de la eleccion del usuario se retorna el diccionario de la pelicula elegida
    5.Si no se encuentran coincidencias, se informa al usuario y se retorna 0

    Informacion complementaria:
    Usamos re.compile para compilar todas las opciones de busqueda
    Usamos re.escape para evitar que caracteres especiales rompan la busqueda
    Usamos re.IGNORECASE para que no diferencie entre mayusculas y minusculas
"""
def buscarPelicula(usuario):
    peliculaABuscar = input("Ingrese el nombre de la película a buscar o 0 para cancelar la operacion").strip().lower()
    while peliculaABuscar == "":
        peliculaABuscar = input("La busqueda no puede estar vacía. Ingrese el nombre de la película a buscar: ").strip().lower()
    patron = re.compile(re.escape(peliculaABuscar), re.IGNORECASE)
    resultados = [p for p in listaPeliculas if patron.search(p["titulo"].lower())]

    if peliculaABuscar != "0":
        if resultados:
            print("Resultados encontrados:")
            for i in range(len(resultados)):
                print(f"{i+1}. {resultados[i]['titulo']}")
            print("")
            numeroPeliculaElegida = int(input("Seleccione el número de la película deseada o 0 para cancelar la operacion: "))
            while numeroPeliculaElegida < 0 or numeroPeliculaElegida > len(resultados):
                numeroPeliculaElegida = int(input("Número inválido. Seleccione un número de la lista brindada: "))
            if numeroPeliculaElegida != 0:
                seleccionada = resultados[numeroPeliculaElegida - 1]
                if (usuario["rol"] != "admin"):
                    print(f'Título: {seleccionada["titulo"]} \nAño: {seleccionada["estreno"]} \nDirector: {seleccionada["director"]} \nGénero(s): {seleccionada["generos"]} \nPóster:  {"No disponible" if seleccionada["poster"] == "" else seleccionada["poster"]} \nSinopsis: {seleccionada["sinopsis"]}')
                return seleccionada
            else:
                print("Operación cancelada.")
                return "0"
        else:
            print(f"No se encontraron resultados para '{peliculaABuscar}'.")
            return "0"
    else:
        print("Operación cancelada.")
        return "0"


