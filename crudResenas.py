from funcionesFile import traerJson, convertirJson


# Helpers JSON
# Trae todas las reseñas guardadas
# Lee el archivo resenas.json y devuelve una lista con todos los datos
def obtenerResenas():
    return traerJson("resenas.json")

# Guarda la lista de reseñas en el archivo json
# Recibe una lista y la escribe en el archivo resenas.json
def guardarResenas(lista):
    convertirJson("resenas.json", lista)


# FUNCIÓN DE ESTADÍSTICAS
# Calcula y muestra el promedio de puntuaciones de cada película
# Recorre todas las reseñas, agrupa por película y calcula el promedio de sus puntuaciones
def estadisticasPuntuaciones():
    listaResenas = obtenerResenas()

    print("\n----- Estadísticas de puntuaciones -----")

    if len(listaResenas) == 0:
        print("No hay reseñas registradas todavía.\n")
        return

    estadisticas = {}

    for r in listaResenas:
        pelicula = r["pelicula"]
        puntuacion = r["puntuacion"]

        if pelicula not in estadisticas:
            estadisticas[pelicula] = {"total": 0, "cantidad": 0}

        estadisticas[pelicula]["total"] += puntuacion
        estadisticas[pelicula]["cantidad"] += 1

    print("Película" + " " * 40 + "Promedio   Cantidad reseñas")
    print("-" * 70)

    for pelicula, datos in estadisticas.items():
        promedio = datos["total"] / datos["cantidad"]
        espacios = 60 - len(pelicula)
        espacios = max(1, espacios)

        print(
            pelicula + " " * espacios +
            str(round(promedio, 2)) + " " * 10 + str(datos["cantidad"])
        )

    print("")

# Muestra las estadísticas de puntuaciones de cada pelicula
# Función auxiliar que llama a estadisticasPuntuaciones para mostrar los datos
def mostrarEstadisticas():
    estadisticasPuntuaciones()


# Crear reseña
# Permite a un usuario crear una nueva reseña de una película
# Solicita los datos al usuario, valida que no haya duplicados y guarda en el archivo
def crearResenas():
    print("\n----- Crear reseñas -----")

    listaResenas = obtenerResenas()
    listaUsuarios = traerJson("usuarios.json")

    continuar = "si"

    while continuar.lower() == "si":

        nuevo_id = max([r["id"] for r in listaResenas], default=0) + 1

        usuario = input("Ingrese el nombre de usuario: ").strip()
        while usuario == "":
            usuario = input("El usuario no puede estar vacío: ").strip()

        pelicula = input("Ingrese el título de la película: ").strip()
        while pelicula == "":
            pelicula = input("El título no puede estar vacío: ").strip()

        # evitar reseñas duplicadas
        for r in listaResenas:
            if r["usuario"].lower() == usuario.lower() and r["pelicula"].lower() == pelicula.lower():
                print(f"El usuario '{usuario}' ya reseñó la película '{pelicula}'.")
                continuar = input("¿Intentar otra reseña? (Si/No): ")
                break
        else:
            # puntuación
            try:
                puntuacion = float(input("Puntuación (0 a 10): "))
            except:
                puntuacion = -1

            while puntuacion < 0 or puntuacion > 10:
                puntuacion = float(input("Debe ser entre 0 y 10: "))

            titulo = input("Título de la reseña: ").strip()
            while titulo == "":
                titulo = input("El título no puede estar vacío: ").strip()

            comentario = input("Comentario: ").strip()
            while comentario == "":
                comentario = input("El comentario no puede estar vacío: ").strip()

            nueva = {
                "id": nuevo_id,
                "usuario": usuario,
                "pelicula": pelicula,
                "puntuacion": puntuacion,
                "titulo": titulo,
                "comentario": comentario
            }

            listaResenas.append(nueva)
            guardarResenas(listaResenas)

            print(f"Reseña creada con ID {nuevo_id}.\n")

            # actualizar contador usuario
            for u in listaUsuarios:
                if u["usuario"].lower() == usuario.lower():
                    u["cantidad_resenas"] = u.get("cantidad_resenas", 0) + 1
                    break

            convertirJson("usuarios.json", listaUsuarios)
            print(f"Se actualizó el contador de reseñas de '{usuario}'.")

        continuar = input("¿Crear otra reseña? (Si/No): ")
        while continuar.lower() not in ["si", "no"]:
            continuar = input("Respuesta inválida: ")


# Mostrar reseñas
# Muestra en pantalla todas las reseñas registradas
# Lee el archivo de reseñas y recorre la lista imprimiendo cada una con sus detalles
def mostrarResenas():
    listaResenas = obtenerResenas()

    print("\n----- Listado de reseñas -----")

    if not listaResenas:
        print("No hay reseñas cargadas.\n")
        return

    for r in listaResenas:
        print(f"ID: {r['id']}")
        print(f"Usuario: {r['usuario']}")
        print(f"Película: {r['pelicula']}")
        print(f"Puntuación: {r['puntuacion']}")
        print(f"Título: {r['titulo']}")
        print(f"Comentario: {r['comentario']}")
        print("-------------------------")

    print("")


# Menú CRUD
# Menú principal para gestionar reseñas de películas
# Muestra las opciones disponibles en un bucle hasta que el usuario elija volver
def crudResenas(usuario):
    print(f"\nUsuario: {usuario['usuario']}  |  Reseñas: {usuario['cantidad_resenas']}")
    opcion = -1

    while opcion != 4:
        print("\n----- Gestión de Reseñas -----")
        print("1. Crear reseña")
        print("2. Mostrar reseñas")
        print("3. Ver estadísticas de puntuaciones")
        print("4. Volver")

        try:
            opcion = int(input("Opción: "))
        except:
            opcion = -1

        if opcion == 1:
            crearResenas()
        elif opcion == 2:
            mostrarResenas()
        elif opcion == 3:
            mostrarEstadisticas()
        elif opcion == 4:
            return
        else:
            print("Opción inválida.")
