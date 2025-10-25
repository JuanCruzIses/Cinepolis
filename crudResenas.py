# Import de lista de reseñas contenido en db.py
from db import listaResenas


# Gestión de Reseñas
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
            while continuar.lower() not in ["si", "no"]:
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

        # TUPLA
        datos_resena = (nuevo_id, usuario, pelicula, puntuacion, titulo_resena, comentario)

        nueva_resena = {
            "id": datos_resena[0],
            "usuario": datos_resena[1],
            "pelicula": datos_resena[2],
            "puntuacion": datos_resena[3],
            "titulo": datos_resena[4],
            "comentario": datos_resena[5]
        }

        listaResenas.append(nueva_resena)
        print(f"La reseña de '{pelicula}' por '{usuario}' fue creada exitosamente con ID {nuevo_id}.\n")

        continuar = input("¿Desea crear otra reseña? (Si / No): ")
        while continuar.lower() not in ["si", "no"]:
            continuar = input("Respuesta inválida. Responda 'Si' o 'No': ")


def mostrarResenas():
    print("")
    print("----- Listado de reseñas -----")
    for resena in listaResenas:
        datos = (resena["id"], resena["usuario"], resena["pelicula"], resena["puntuacion"], resena["titulo"], resena["comentario"])
        id, usuario, pelicula, puntuacion, titulo, comentario = datos  # desempaquetado

        print(f"ID: {id}\nUsuario: {usuario}\nPelícula: {pelicula}\nPuntuación: {puntuacion}\nTítulo: {titulo}\nComentario: {comentario}")
        print("-------------------------------\n")


def crudResenas(usuario):
    if usuario != 0 and usuario != None:
        print(f'Usuario: {usuario["usuario"]} \nReseñas: {usuario["cantidad_resenas"]}')
    print("")
    print("----- Gestión de Reseñas -----")
    print("1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menú principal")
    opcion = int(input("Seleccione la opción: "))
    while opcion != 3:
        if opcion == 1:
            crearResenas()
        elif opcion == 2:
            mostrarResenas()
        else:
            print("Opción inválida")
        print("\n1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menú principal")
        opcion = int(input("Seleccione la opción: "))
        print(" ")
    return
