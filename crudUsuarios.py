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
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i]["email"] == email:
            print("Este email ya se encuentra registrado.")
            return
    
    contraseña = input("Ingrese contraseña: ")
    while len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        contraseña = input("Ingrese contraseña (mínimo 8 caracteres): ")

    confirmarContrasena = input("Confirme la contraseña: ")
    while contraseña != confirmarContrasena:
        print("Las contraseñas no coinciden. Intente nuevamente.")
        confirmarContrasena = input("Confirme la contraseña: ")

    img = input("Ingrese URL de imagen (opcional): ")

    nuevo_usuario = {
        "id": nuevo_id,
        "usuario": usuario,
        "email": email,
        "img": img,
        "cantidad_reseñas": 0,
        "contraseña": contraseña,
        "rol": "user"
    }

    listaUsuarios.append(nuevo_usuario)
    print("Usuario '" + usuario + "' creado exitosamente con ID " + str(nuevo_id))
    return


def iniciarSesion():
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    usuario_encontrado = list(filter(lambda u: u["email"] == email, listaUsuarios))
    if len(usuario_encontrado) == 0:
        print("No se encontró un usuario con ese email.")
        print("")
        return 0
    
    if usuario_encontrado[0]["contraseña"] == contraseña:
        print("Inicio de sesion exitoso, bienvenido " + usuario_encontrado[0]["usuario"])
        print("")
        return usuario_encontrado[0]
    else:
        print("Contraseña incorrecta.")
        print("")
        return 0

def editarUsuario(usuario):
    if usuario == 0 or usuario == None:
        print("Debe iniciar sesión para editar su perfil")
        print("")
        return
    
    usuario_obj = list(filter(lambda u: u["id"] == usuario["id"], listaUsuarios))
    
    if len(usuario_obj) == 0:
        print("No se encontró un usuario con ese ID")
        print("")
        return

    print("Deja el campo vacio si no queres cambiarlo")
    nuevo_usuario = input(f"Nuevo nombre de usuario (actual: {usuario_obj[0]['usuario']}): ")
    nuevo_email = input(f"Nuevo email (actual: {usuario_obj[0]['email']}): ")
    nueva_img = input(f"Nueva url de imagen (actual: {usuario_obj[0]['img']}): ")
    nueva_contraseña = input("Nueva contraseña: ")

    if nuevo_usuario != "":
        usuario_obj[0]["usuario"] = nuevo_usuario
    if nuevo_email != "":
        usuario_obj[0]["email"] = nuevo_email
    if nueva_img != "":
        usuario_obj[0]["img"] = nueva_img
    if nueva_contraseña != "":
        usuario_obj[0]["contraseña"] = nueva_contraseña

    print("El usuario ha sido actualizado correctamente")
    print("")
    return

def eliminarUsuario(usuario):
    usuario_eliminar = usuario["usuario"]
    
    usuario_obj = ""
    for u in listaUsuarios:
        if u["usuario"].lower() == usuario_eliminar.lower():
            usuario_obj = u
            break

    if not usuario_obj:
        print("No se encontró un usuario con ese nombre.")
        print("")
        return
    else:
        print(f"El usuario '{usuario_eliminar}' será eliminado.")
        confirmacion = input("Para confirmar la eliminacion responda 'Si' o 'No': ")
        while confirmacion.lower() != "si" and confirmacion.lower() != "no":
            confirmacion = input("Respuesta inválida. Responda 'Si' o 'No': ")
        if confirmacion.lower() == "si":
            i = 0
            while i < len(listaResenas):
                if listaResenas[i]["usuario"].lower() == usuario_eliminar.lower():
                    del listaResenas[i]
                else:
                    i += 1

            listaUsuarios.remove(usuario_obj)

            print(f"El usuario '{usuario_eliminar}' y sus reseñas han sido eliminados correctamente.")
            usuario = 0
            return usuario
        else:
            print("Operación de eliminación cancelada.")
            return

def cerrarSesion(usuario):
    if usuario == 0 or usuario == None:
        print("No hay ninguna sesión iniciada")
        print("")
        return 0
    
    print(f"Sesión de {usuario['usuario']} cerrada correctamente")
    print("")
    return 0

def editarUsuarioAdmin():
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
    print("")
    return

def eliminarUsuarioAdmin():

    usuario_eliminar = input("Ingrese el nombre de usuario a eliminar: ")
    
    usuario_obj = ""
    for u in listaUsuarios:
        if u["usuario"].lower() == usuario_eliminar.lower():
            usuario_obj = u
            break

    if not usuario_obj:
        print("No se encontró un usuario con ese nombre.")
        print("")
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
    print("")
    return

def crudUsuarios(usuario):
    if usuario != 0 and usuario != None:
        print(f'Usuario: {usuario["usuario"]} \nReseñas: {usuario["cantidad_reseñas"]}')
    print("")
    opcion = 0
    while opcion != 3:
        print("----- CRUD de Usuarios -----")
        #Funciones disponibles si el USUARIO NO INICIO SESION
        if usuario == 0 or usuario == None:
            print("1. Registrarse \n2. Iniciar Sesion \n3. Volver al menu principal")
            opcion = int(input("Seleccione la opcion: "))
            if opcion == 1:
                crearUsuario()
            elif opcion == 2:
                usuario = iniciarSesion()
            elif opcion == 3:
                mostrarUsuarios()
            else:
                print("Opción inválida")
        #Funciones disponibles si el USUARIO INICIO SESION
        else:
            #Funciones disponibles si el USUARIO TIENE ROL 'ADMIN'
            if usuario["rol"] == "admin":
                print("1. Editar usuario \n2. Eliminar usuario \n3. Mostrar usuarios \n4. Cerrar sesión \n5. Volver al menu principal")
                opcion = int(input("Seleccione la opcion: "))
                while opcion != 5:
                    if opcion == 1:
                        editarUsuarioAdmin()
                    elif opcion == 2:
                        eliminarUsuarioAdmin()
                    elif opcion == 3:
                        mostrarUsuarios()
                    elif opcion == 4:
                        usuario = cerrarSesion(usuario)
                        return usuario
                    else:
                        print("Opción inválida")
                    
                    print("1. Editar usuario \n2. Eliminar usuario \n3. Mostrar usuarios \n4. Cerrar sesión \n5. Volver al menu principal")
                    opcion = int(input("Seleccione la opcion: "))
            #Funciones disponibles si el USUARIO TIENE ROL 'USER'            
            else:
                print("1. Editar usuario \n2. Eliminar usuario \n3. Cerrar sesión \n4. Volver al menu principal")
                opcion = int(input("Seleccione la opcion: "))
                while opcion != 4:
                    if opcion == 1:
                        editarUsuario(usuario)
                    elif opcion == 2:
                        usuario = eliminarUsuario(usuario)
                        if usuario == 0:
                            return usuario
                    elif opcion == 3:
                        usuario = cerrarSesion(usuario)
                        return usuario
                    else:
                        print("Opción inválida")
                    
                    print("1. Editar usuario \n2. Eliminar usuario \n3. Cerrar sesión \n4. Volver al menu principal")
                    opcion = int(input("Seleccione la opcion: "))

    return usuario
