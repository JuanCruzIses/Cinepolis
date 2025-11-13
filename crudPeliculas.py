#Imports necesarios para el CRUD 
# from db import listaPeliculas
from funcionesGenerales import buscarPelicula 
import os
from funcionesFile import convertirJson, traerJson

# ---> Funciones para la gestión de películas (CRUD) <---
"""
Gestión de Películas (CRUD)
    -Crear, editar, eliminar y mostrar películas.
    -Campos: id, título, estreno, director, géneros, sinopsis.
    -Listado paginado básico.
"""
def crearPelicula():
    print("")
    print("----- Crear películas -----")

    listaPeliculas = traerJson("peliculas.json")
    continuar = "si"
    while continuar.lower() == "si":
        if listaPeliculas:
            nuevo_id = max(p["id"] for p in listaPeliculas) + 1
        else:
            nuevo_id = 1

        titulo = input("Ingrese el título de la película: ")
        while titulo == "":
            titulo = input("El título no puede estar vacío. Ingrese el título: ")

        existe = False
        for p in listaPeliculas:
            if p["titulo"].lower() == titulo.lower():
                existe = True
        if existe:
            print("Ya existe una película con ese título.")
            continuar = input("¿Desea intentar con otra película? Si o No: ")
            while continuar.lower() not in ["si", "no"]:
                continuar = input("Respuesta inválida. Responda Si o No: ")
            continue

        estreno = input("Ingrese el año de estreno: ")
        while not estreno.isdigit():
            print("Debe ingresar un número válido para el año.")
            estreno = input("Ingrese el año de estreno: ")
        estreno = int(estreno)

        director = input("Ingrese el director: ")
        while director == "":
            director = input("El director no puede estar vacío. Ingrese el director: ")

        generos_texto = input("Ingrese los géneros (separados por comas): ")
        while generos_texto == "":
            generos_texto = input("Debe ingresar al menos un género: ")
        
        generos = set(g.strip() for g in generos_texto.split(","))

        sinopsis = input("Ingrese la sinopsis (opcional): ")
        poster = input("Ingrese la URL del póster (opcional): ")

        # TUPLA
        datos_pelicula = (nuevo_id, titulo, estreno, director)

        nueva_pelicula = {
            "id": datos_pelicula[0],
            "titulo": datos_pelicula[1],
            "estreno": datos_pelicula[2],
            "director": datos_pelicula[3],
            "generos": list(generos),
            "sinopsis": sinopsis,
            "poster": poster
        }

        listaPeliculas.append(nueva_pelicula)
        convertirJson("peliculas.json", listaPeliculas)
        print("La película '" + nueva_pelicula["titulo"] + "' fue creada exitosamente con ID " + str(nueva_pelicula["id"]) + ".")
        # Mostrar detalles de la película recién creada
        print("Detalles de la película creada:")
        print(f"ID: {nueva_pelicula['id']}\nTítulo: {nueva_pelicula['titulo']}\nEstreno: {nueva_pelicula['estreno']}\nDirector: {nueva_pelicula['director']}")
        print(f"Géneros: {', '.join(nueva_pelicula.get('generos', []))}\nSinopsis: {nueva_pelicula.get('sinopsis', '')}\nPóster: {nueva_pelicula.get('poster', '')}")
        print("")

        continuar = input("¿Desea crear otra película? (Si / No): ")
        while continuar.lower() not in ["si", "no"]:
            continuar = input("Respuesta inválida. Responda 'Si' o 'No': ")        


def mostrarPeliculas():
    print("")
    print("----- Listado de películas -----")
    listaPeliculas = traerJson("peliculas.json")

    if len(listaPeliculas) == 0:
        print("No hay películas registradas.")
        print("")
        return

    accion = input("¿Desea aplicar un filtro u orden? (Filtro / Orden / No): ")
    while accion.lower() not in ["filtro", "orden", "no"]:
        accion = input("Respuesta inválida. Responda 'Filtro', 'Orden' o 'No': ")

    if accion.lower() == "filtro":
        print("Filtrar por:\n1. Género\n2. Director")
        opcion = input("Seleccione una opción: ")

        while opcion not in ["1", "2"]:
            opcion = input("Opción inválida. Seleccione 1 o 2: ")

        peliculas_filtradas = []

        if opcion == "1":
            genero = input("Ingrese el género a buscar: ").lower()
            for pelicula in listaPeliculas:
                for g in pelicula["generos"]:
                    if genero in g.lower():
                        peliculas_filtradas.append(pelicula)

        elif opcion == "2":
            director = input("Ingrese el nombre del director: ").lower()
            for pelicula in listaPeliculas:
                if director in pelicula["director"].lower():
                    peliculas_filtradas.append(pelicula)

        listaPeliculas = peliculas_filtradas

    elif accion.lower() == "orden":
        print("Ordenar por:\n1. Año de estreno\n2. Título (alfabéticamente)")
        opcion = input("Seleccione una opción: ")

        while opcion not in ["1", "2"]:
            opcion = input("Opción inválida. Seleccione 1 o 2: ")

        if opcion == "1":
            listaPeliculas = sorted(listaPeliculas, key=lambda x: x["estreno"])
        elif opcion == "2":
            listaPeliculas = sorted(listaPeliculas, key=lambda x: x["titulo"].lower())

    if len(listaPeliculas) == 0:
        print("No se encontraron películas con ese criterio.")
        print("")
        return

    for pelicula in listaPeliculas:
        datos = (pelicula["id"], pelicula["titulo"], pelicula["estreno"], pelicula["director"])
        id, titulo, estreno, director = datos

        generos = ", ".join(pelicula["generos"])
        sinopsis = pelicula["sinopsis"]
        poster = pelicula["poster"]

        print(f"ID: {id}\nTítulo: {titulo}\nEstreno: {estreno}\nDirector: {director}\nGéneros: {generos}\nSinopsis: {sinopsis}\nPóster: {poster}")
        print("-------------------------------\n")




#----> Editar película <----
def editarPelicula(usuario):
    print("")
    print("----- Editar películas -----")
    pelicula_a_editar = buscarPelicula(usuario)
    listaPeliculas = traerJson("peliculas.json")

    while pelicula_a_editar != "0":
        print("Editando la película:", pelicula_a_editar["titulo"])

        if pelicula_a_editar == False:
            print("La película ingresada no fue encontrada.")
            pelicula_a_editar = input('Ingrese el título de otra película a editar o "0" para salir: ')

        nuevo_titulo = input("Nuevo título (Enter para mantener el actual): ")
        if nuevo_titulo != "":
            pelicula_a_editar["titulo"] = nuevo_titulo

        nuevo_estreno = input("Nuevo año de estreno (Enter para mantener el actual): ")
        if nuevo_estreno != "":
            if nuevo_estreno.isdigit():
                pelicula_a_editar["estreno"] = int(nuevo_estreno)
            else:
                print("El año ingresado no es válido. Se mantiene el anterior.")

        nuevo_director = input("Nuevo director (Enter para mantener el actual): ")
        if nuevo_director != "":
            pelicula_a_editar["director"] = nuevo_director

        nuevos_generos = input("Nuevos géneros (separados por comas, Enter para mantener los actuales): ")
        if nuevos_generos != "":
            pelicula_a_editar["generos"] = nuevos_generos.split(",")

        nueva_sinopsis = input("Nueva sinopsis (Enter para mantener la actual): ")
        if nueva_sinopsis != "":
            pelicula_a_editar["sinopsis"] = nueva_sinopsis

        nuevo_poster = input("Nueva URL del póster (Enter para mantener la actual): ")
        if nuevo_poster != "":
            pelicula_a_editar["poster"] = nuevo_poster

        for pelicula in listaPeliculas:
            if pelicula["titulo"].lower() == pelicula_a_editar["titulo"].lower():
                pelicula = pelicula_a_editar
        
        convertirJson("peliculas.json", listaPeliculas)
        print("La película fue actualizada correctamente.")
        print("")

        pelicula_a_editar = input('Ingrese el título de otra película a editar o "0" para salir: ')
    

#----> Eliminar película <----
def eliminarPelicula(usuario):
    print("")
    print("----- Eliminar películas -----")
    pelicula_a_eliminar = buscarPelicula(usuario)
    listaPeliculas = traerJson("peliculas.json")

    while pelicula_a_eliminar != "0":
        peliculaEncontrada = True
        print(f'¿Seguro que desea eliminar la película {pelicula_a_eliminar["titulo"]}?')
        confirmacion = input("Responda 'Si' o 'No': ")
        while confirmacion.lower() != "si" and confirmacion.lower() != "no":
            confirmacion = input("Respuesta inválida. Responda 'Si' o 'No': ")
        if confirmacion.lower() == "si":
            listaPeliculas.remove(pelicula_a_eliminar)
            convertirJson("peliculas.json", listaPeliculas)
            print("La película fue eliminada correctamente.")
        else:
            print("Operación de eliminación cancelada.")

        if peliculaEncontrada == False:
            print("La película '" + pelicula_a_eliminar["titulo"] + "' no fue encontrada.")

        pelicula_a_eliminar = buscarPelicula(usuario)


def crudPeliculas(usuario):
    opcionElegida = 0
    while opcionElegida != 5:
        print("----- CRUD de Películas -----")
        #Funciones disponibles si el USUARIO NO INICIO SESION
        if usuario == 0 or usuario == None:
            print('Usuario no logueado')
            print('')
            print("Debes iniciar sesión para acceder a las funciones de películas.")
            opcionElegida = 5
        #Funciones disponibles si el USUARIO INICIO SESION
        else:
            #Funciones disponibles si el USUARIO TIENE ROL 'ADMIN'
            if usuario["rol"] == "admin":
                print("1. Crear película \n2. Editar película \n3. Eliminar película \n4. Mostrar películas \n5. Volver al menú principal")
                opcionElegida = int(input("Seleccione la opción a ejecutar:"))

                if opcionElegida == 1:
                    crearPelicula()
                elif opcionElegida == 2:
                    editarPelicula(usuario)
                elif opcionElegida == 3:
                    eliminarPelicula(usuario)
                elif opcionElegida == 4:
                    mostrarPeliculas()
                else:
                    print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
                print(" ")
            
            #Funciones disponibles si el USUARIO TIENE ROL 'USER'            
            else:
                print("1. Buscar películas \n2. Mostrar películas \n3. Volver al menú principal")            
                opcionElegida = int(input("Seleccione la opción a ejecutar: "))

                if opcionElegida == 1:
                    buscarPelicula(usuario)
                elif opcionElegida == 2:
                    mostrarPeliculas()
                elif opcionElegida == 3:
                    opcionElegida = 5
                else:
                    print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
                print(" ")
        print(" ")
    return
