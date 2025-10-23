# Import de lista de usuarios y reseñas contenido en db.py
from db import listaUsuarios, listaResenas

# Gestión de Usuarios (CRUD)
def crearUsuario():
    if len(listaUsuarios) == 0:
        nuevo_id = 1
    else:
        nuevo_id = listaUsuarios[-1]["id"] + 1  # agarro el último id y le agrego 1

    usuario = input("Ingrese nombre de usuario: ")
    while usuario == "":
        usuario = input("El usuario no puede estar vacío. Ingrese nombre de usuario: ")

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
    # TUPLA
    datos_usuario = (nuevo_id, usuario, email, img, contraseña)

    nuevo_usuario = {
        "id": datos_usuario[0],
        "usuario": datos_usuario[1],
        "email": datos_usuario[2],
        "img": datos_usuario[3],
        "cantidad_reseñas": 0,
        "contraseña": datos_usuario[4],
        "rol": "user"
    }

    listaUsuarios.append(nuevo_usuario)
    print(f"Usuario '{usuario}' creado exitosamente con ID {nuevo_id}")
    return


def iniciarSesion():
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    usuario_encontrado = None
    for u in listaUsuarios:
        if u["email"] == email:
            usuario_encontrado = u

    if usuario_encontrado is None:
        print("No se encontró un usuario con ese email.")
        print("")
        return 0
    
    if usuario_encontrado["contraseña"] == contraseña:
        print(f"Inicio de sesión exitoso, bienvenido {usuario_encontrado['usuario']}")
        print("")
        return usuario_encontrado
    else:
        print("Contraseña incorrecta.")
        print("")
        return 0


def editarUsuario(usuario):
    if usuario == 0 or usuario == None:
        print("Debe iniciar sesión para editar su perfil")
        print("")
        return
    
    usuario_obj = None
    for u in listaUsuarios:
        if u["id"] == usuario["id"]:
            usuario_obj = u

    if usuario_obj is None:
        print("No se encontró un usuario con ese ID")
        print("")
        return

    print("Deje el campo vacío si no quiere cambiarlo")
    nuevo_usuario = input(f"Nuevo nombre (actual: {usuario_obj['usuario']}): ")
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

    print("El usuario ha sido actualizado correctamente\n")
    return


def eliminarUsuario(usuario):
    if usuario == 0 or usuario == None:
        print("Debe iniciar sesión para eliminar su cuenta\n")
        return usuario
    
    usuario_obj = None
    for u in listaUsuarios:
        if u["id"] == usuario["id"]:
            usuario_obj = u

    if usuario_obj is None:
        print("Error: No se encontró la información del usuario\n")
        return usuario

    print(f"El usuario '{usuario['usuario']}' será eliminado.")
    confirmacion = input("Para confirmar la eliminación responda 'Si' o 'No': ")
    while confirmacion.lower() not in ["si", "no"]:
        confirmacion = input("Respuesta inválida. Responda 'Si' o 'No': ")

    if confirmacion.lower() == "si":
        i = 0
        while i < len(listaResenas):
            if listaResenas[i]["usuario"].lower() == usuario["usuario"].lower():
                del listaResenas[i]
            else:
                i += 1
    
        listaUsuarios.remove(usuario_obj)
        print(f"El usuario '{usuario['usuario']}' y sus reseñas han sido eliminados correctamente.\n")
        return 0
    else:
        print("Operación de eliminación cancelada.\n")
        return usuario


def cerrarSesion(usuario):
    if usuario == 0 or usuario == None:
        print("No hay ninguna sesión iniciada\n")
        return 0
    
    print(f"Sesión de {usuario['usuario']} cerrada correctamente\n")
    return 0


def mostrarUsuarios():
    print("----- Listado de usuarios -----")
    if len(listaUsuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for u in listaUsuarios:
        datos = (u["id"], u["usuario"], u["email"], u["img"], u["cantidad_reseñas"], u["rol"])
        id, usuario, email, img, cantidad_reseñas, rol = datos

        print(f"ID: {id} | Usuario: {usuario} | Email: {email} | Img: {img} | Reseñas: {cantidad_reseñas} | Rol: {rol}")
    print("")
    return


def crudUsuarios(usuario):
    if usuario != 0 and usuario != None:
        print(f'Usuario: {usuario["usuario"]} \nReseñas: {usuario["cantidad_reseñas"]}')
    print("")
    ejecuta = True
    while ejecuta != False:
        print("----- CRUD de Usuarios -----")
        #Funciones disponibles si el USUARIO NO INICIO SESION
        if usuario == 0 or usuario == None:
            print("1. Registrarse \n2. Iniciar Sesion \n3. Mostrar usuarios \n4. Volver al menu principal")
            opcion = int(input("Seleccione la opcion: "))
            if opcion == 1:
                crearUsuario()
            elif opcion == 2:
                usuario = iniciarSesion()
            elif opcion == 3:
                mostrarUsuarios()
            elif opcion == 4:
                ejecuta = False
            else:
                print("Opción inválida")
        #Funciones disponibles si el USUARIO INICIO SESION
        else:
            #Funciones disponibles si el USUARIO TIENE ROL 'ADMIN'
            if usuario["rol"] == "admin":
                print("1. Editar usuario \n2. Eliminar usuario \n3. Mostrar usuarios \n4. Cerrar sesión \n5. Volver al menu principal")
                opcion = int(input("Seleccione la opcion: "))
                if opcion == 1:
                    editarUsuarioAdmin()
                elif opcion == 2:
                    eliminarUsuarioAdmin()
                elif opcion == 3:
                    mostrarUsuarios()
                elif opcion == 4:
                    usuario = cerrarSesion(usuario)
                    return usuario
                elif opcion == 5:
                    ejecuta = False
                else:
                    print("Opción inválida")
                
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
                    elif opcion == 4:
                        ejecuta = False
                    else:
                        print("Opción inválida")
                    
                return usuario

    # if usuario != 0 and usuario != None:
    return usuario
