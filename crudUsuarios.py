#Import de lista de usuarios y reseñas contenido en db.py
from db import listaUsuarios, listaResenas

# Gestión de Usuarios (CRUD)
def crearUsuario():
    if len(listaUsuarios) == 0:
        nuevo_id = 1
    else:
        nuevo_id = listaUsuarios[-1]["id"] + 1  # agarro el ultimo id y le agrego 1

    usuario = input("Ingrese nombre de usuario: ")
    while usuario == "":
        usuario = input("El usuario no puede estar vacio. Ingrese nombre de usuario: ")

    for i in range(len(listaUsuarios)):
        if listaUsuarios[i]["usuario"] == usuario:
            print("Ya existe un usuario con ese nombre.")
            return

    email = input("Ingrese email: ")
    contraseña = input("Ingrese contraseña: ")
    img = input("Ingrese URL de imagen (opcional): ")

    nuevo_usuario = {
        "id": nuevo_id,
        "usuario": usuario,
        "email": email,
        "img": img,
        "cantidad_reseñas": 0,
        "contraseña": contraseña
    }

    listaUsuarios.append(nuevo_usuario)
    print("Usuario '" + usuario + "' creado exitosamente con ID " + str(nuevo_id))
    return


def iniciarSesion():
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    for i in range(len(listaUsuarios)):
        if listaUsuarios[i]["email"] == email:
            if listaUsuarios[i]["contraseña"] == contraseña:
                print("Inicio de sesion exitoso, bienvenido " + listaUsuarios[i]["usuario"])
                return listaUsuarios[i]
            else:
                print("Contraseña incorrecta.")
                return 0

def editarUsuario():
    nombre_usuario = input("Ingrese el nombre de usuario que desea editar: ")

    usuario_obj = None
    for u in listaUsuarios:
        if u["usuario"].lower() == nombre_usuario.lower():
            usuario_obj = u

    if usuario_obj is None:
        print("No se encontro un usuario con ese nombre")
        return

    print("Deja el campo vacio si no queres cambiarlo")
    nuevo_usuario = input(f"Nuevo nombre de usuario (actual: {usuario_obj['usuario']}): ")
    nuevo_email = input(f"Nuevo email (actual: {usuario_obj['email']}): ")
    nueva_img = input(f"Nueva url de imagen (actual: {usuario_obj['img']}): ")
    nueva_contraseña = input("Nueva contraseña: ")

    if nuevo_usuario != "":
        usuario_obj["usuario"] = nuevo_usuario
    if nuevo_email != "":
        usuario_obj["email"] = nuevo_email
    if nueva_img != "":
        usuario_obj["img"] = nueva_img
    if nueva_contraseña != "":
        usuario_obj["contraseña"] = nueva_contraseña

    print("El usuario ha sido actualizado correctamente")
    return

def eliminarUsuario():

    usuario_eliminar = input("Ingrese el nombre de usuario a eliminar: ")
    
    usuario_obj = ""
    for u in listaUsuarios:
        if u["usuario"].lower() == usuario_eliminar.lower():
            usuario_obj = u
            break

    if not usuario_obj:
        print("No se encontró un usuario con ese nombre.")
        return
    
    i = 0
    while i < len(listaResenas):
        if listaResenas[i]["usuario"].lower() == usuario_eliminar.lower():
            del listaResenas[i]
        else:
            i += 1

    listaUsuarios.remove(usuario_obj)

    print(f"El usuario '{usuario_eliminar}' y sus reseñas han sido eliminados correctamente.")
    return

def mostrarUsuarios():
    print("----- Listado de usuarios -----")
    if len(listaUsuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for u in listaUsuarios:
        print("ID:", u["id"], "| Usuario:", u["usuario"], "| Email:", u["email"], "| Img:", u["img"], "| Reseñas:", u["cantidad_reseñas"])
    return

def crudUsuarios(usuario):
    print(" ")
    print("----- CRUD de Usuarios -----")
    print("1. Crear usuario \n2. Iniciar Sesion \n3. Editar usuario \n4. Eliminar usuario \n5. Mostrar usuarios \n6. Volver al menu principal")
    opcion = int(input("Seleccione la opcion: "))
    while opcion != 6:
        if opcion == 1:
            crearUsuario()
        elif opcion == 2:
            usuario = iniciarSesion()
        elif opcion == 3:
            editarUsuario()
        elif opcion == 4:
            eliminarUsuario()
        elif opcion == 5:
            mostrarUsuarios()
        else:
            print("Opción inválida")
        
        print(" ")
        print("1. Crear usuario \n2. Iniciar Sesion \n3. Editar usuario \n4. Eliminar usuario \n5. Mostrar usuarios \n6. Volver al menu principal")
        opcion = int(input("Seleccione la opcion: "))
        print("")

    if usuario:
        return usuario
    return
