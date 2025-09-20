#Import de lista de resenas contenido en db.py
from db import listaResenas


# Gestion de Reseñas
def crearResenas():
    print("")
    print("----- Crear reseñas -----")

    continuar = "si"
    while continuar.lower() == "si":
        if listaResenas:
            nuevo_id = max(r["id"] for r in listaResenas) + 1
        else:
            nuevo_id = 1

        usuario = input("Ingrese el nombre de usuario: ")
        while usuario == "":
            usuario = input("El usuario no puede estar vacío. Ingrese el nombre de usuario: ")

        pelicula = input("Ingrese el título de la película a reseñar: ")
        while pelicula == "":
            pelicula = input("El título de la película no puede estar vacío. Ingrese el título: ")

        existe = False
        for r in listaResenas:
            if r["usuario"].lower() == usuario.lower() and r["pelicula"].lower() == pelicula.lower():
                existe = True
        if existe:
            print(f"El usuario '{usuario}' ya realizó una reseña para '{pelicula}'.")
            continuar = input("¿Desea intentar con otra reseña? Si o No: ")
            while continuar.lower() != "si" and continuar.lower() != "no":
                continuar = input("Respuesta inválida. Responda Si o No: ")
            continue

        puntuacion = float(input("Ingrese la puntuación (0 a 10): "))
        while puntuacion < 0 or puntuacion > 10:
            print("La puntuación debe ser un número entre 0 y 10.")
            puntuacion = float(input("Ingrese la puntuación (0 a 10): "))
    

        titulo_resena = input("Ingrese el título de la reseña: ")
        while titulo_resena == "":
            titulo_resena = input("El título no puede estar vacío. Ingrese el título de la reseña: ")

        comentario = input("Ingrese el comentario de la reseña: ")
        while comentario == "":
            comentario = input("El comentario no puede estar vacío. Ingrese el comentario: ")

        nueva_resena = {
            "id": nuevo_id,
            "usuario": usuario,
            "pelicula": pelicula,
            "puntuacion": puntuacion,
            "titulo": titulo_resena,
            "comentario": comentario
        }

        listaResenas.append(nueva_resena)
        print(f"La reseña de '{pelicula}' por '{usuario}' fue creada exitosamente con ID {nuevo_id}.")
        print("")

        continuar = input("¿Desea crear otra reseña? (Si / No): ")
        while continuar.lower() != "si" and continuar.lower() != "no":
            continuar = input("Respuesta inválida. Responda 'Si' o 'No': ")



def mostrarResenas():
    print("")
    print("----- Listado de reseñas -----")
    for resena in listaResenas:
        id = resena["id"]
        usuario = resena["usuario"]
        pelicula = resena["pelicula"]
        puntuacion = resena["puntuacion"]
        titulo = resena["titulo"]
        comentario = resena["comentario"]

        print(f"ID: {id} \nUsuario: {usuario} \nPelícula: {pelicula} \nPuntuación: {puntuacion} \nTítulo: {titulo} \nComentario: {comentario}")
        print("")
        print("-------------------------------")
        print("")

def crudResenas(usuario):
    print("")
    print("----- Gestion de Reseñas -----")
    print("1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menu principal")
    opcion = int(input("Seleccione la opcion: "))
    while opcion != 3:
        if opcion == 1:
            crearResenas()
        elif opcion == 2:
            mostrarResenas()
        else:
            print("Opcion invalida")
        print(" ")
        print("\n1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menu principal")
        opcion = int(input("Seleccione la opcion: "))
        print(" ")
    return
