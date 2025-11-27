import os
from funcionesFile import traerJson
listaUsuarios = traerJson("usuarios.json")

from crudPeliculas import mostrarPeliculas, crearPelicula, editarPelicula, eliminarPelicula
from crudResenas import mostrarResenas, crearResenas
from crudUsuarios import mostrarUsuarios

# COLORES ANSI
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"

current_user = None  # usuario logueado

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    print(f"{CYAN}{BOLD}\n========== {texto} =========={RESET}\n")

def pausar():
    input(f"\n{YELLOW}Presiona ENTER para continuar...{RESET}")

def login():
    global current_user
    limpiar()
    titulo("🔐 INICIAR SESIÓN")

    usuario_ingresado = input("Usuario: ").strip()
    clave_ingresada = input("Clave: ").strip()

    for u in listaUsuarios:
        usuario_json = str(u["usuario"]).strip().lower()
        clave_json = str(u["clave"]).strip()

        if usuario_json == usuario_ingresado.lower() and clave_json == clave_ingresada:
            current_user = u
            print(f"{GREEN}✔ Sesión iniciada correctamente. Bienvenido {u['usuario']}!{RESET}")
            pausar()
            return

    print(f"{RED}❌ Usuario o clave incorrectos{RESET}")
    pausar()



def logout():
    global current_user
    print(f"\n{YELLOW}👋 Sesión cerrada{RESET}")
    current_user = None
    pausar()

def requiere_login():
    if not current_user:
        print(f"\n{RED}🚫 Acceso denegado{RESET}")
        print(f"{YELLOW}Debes iniciar sesión para usar esta función.{RESET}")
        pausar()
        return False
    return True

def requiere_admin():
    if not current_user:
        print(f"\n{RED}🚫 Acceso denegado{RESET}")
        print(f"{YELLOW}Debes iniciar sesión como administrador.{RESET}")
        pausar()
        return False

    if current_user["rol"].lower() != "admin":
        print(f"\n{RED}⛔ No tienes permisos suficientes{RESET}")
        print(f"{YELLOW}Solo un administrador puede realizar esta acción.{RESET}")
        pausar()
        return False

    return True


def menu_principal():
    while True:
        limpiar()
        titulo("🎬 CINEPOLIS - MENÚ PRINCIPAL")

        print(f"{GREEN}1.{RESET} Películas")
        print(f"{GREEN}2.{RESET} Reseñas")
        print(f"{GREEN}3.{RESET} Usuarios")

        if current_user:
            print(f"{GREEN}4.{RESET} Cerrar sesión ({current_user['usuario']})")
        else:
            print(f"{GREEN}4.{RESET} Iniciar sesión")

        print(f"{GREEN}0.{RESET} Salir")

        opcion = input(f"\n{YELLOW}Elegí una opción: {RESET}")

        invalid_input = False
        try:
            opcion_int = int(opcion)
        except ValueError:
            invalid_input = True
            print(f"{RED}⚠️ Opción inválida (debe ingresar un número){RESET}")
            pausar()

        if not invalid_input:
            if opcion_int == 1:
                menu_peliculas()
            elif opcion_int == 2:
                menu_resenas()
            elif opcion_int == 3:
                menu_usuarios()
            elif opcion_int == 4:
                if current_user:
                    logout()
                else:
                    login()
            elif opcion_int == 0:
                limpiar()
                print(f"{CYAN}👋 ¡Gracias por usar Cinepolis!{RESET}\n")
                break
            else:
                print(f"{RED}⚠️ Opción inválida{RESET}")
                pausar()


def menu_peliculas():
    while True:
        limpiar()
        titulo("🎞️ GESTIÓN DE PELÍCULAS")
        print(f"{GREEN}1.{RESET} Mostrar películas")
        print(f"{GREEN}2.{RESET} Crear película")
        print(f"{GREEN}3.{RESET} Editar película")
        print(f"{GREEN}4.{RESET} Eliminar película")
        print(f"{GREEN}0.{RESET} Volver")

        opcion = input(f"\n{YELLOW}Elegí una opción: {RESET}")

        invalid_input = False
        try:
            opcion_int = int(opcion)
        except ValueError:
            invalid_input = True
            print(f"{RED}⚠️ Opción inválida (debe ingresar un número){RESET}")
            pausar()

        if not invalid_input:
            if opcion_int == 1:
                limpiar()
                mostrarPeliculas()
                pausar()
            elif opcion_int == 2:
                if requiere_admin():
                    crearPelicula()
                    pausar()
            elif opcion_int == 3:
                if requiere_admin():
                    try:
                        editarPelicula(current_user)
                    except Exception as e:
                        print(f"{RED}❌ Error al editar película: {e}{RESET}")
                    pausar()
            elif opcion_int == 4:
                if requiere_admin():
                    try:
                        eliminarPelicula(current_user)
                    except Exception as e:
                        print(f"{RED}❌ Error al eliminar película: {e}{RESET}")
                    pausar()
            elif opcion_int == 0:
                break
            else:
                print(f"{RED}⚠️ Opción inválida{RESET}")
                pausar()


def menu_resenas():
    while True:
        limpiar()
        titulo("⭐ GESTIÓN DE RESEÑAS")
        print(f"{GREEN}1.{RESET} Mostrar reseñas")
        print(f"{GREEN}2.{RESET} Crear reseña")
        print(f"{GREEN}3.{RESET} Ver estadísticas de películas")
        print(f"{GREEN}0.{RESET} Volver")

        opcion = input(f"\n{YELLOW}Elegí una opción: {RESET}")

        invalid_input = False
        try:
            opcion_int = int(opcion)
        except ValueError:
            invalid_input = True
            print(f"{RED}⚠️ Opción inválida (debe ingresar un número){RESET}")
            pausar()

        if not invalid_input:
            if opcion_int == 1:
                limpiar()
                mostrarResenas()
                pausar()
            elif opcion_int == 2:
                if requiere_login():
                    try:
                        crearResenas()
                    except Exception as e:
                        print(f"{RED}❌ Error al crear reseña: {e}{RESET}")
                    pausar()
            elif opcion_int == 3:
                limpiar()
                from crudResenas import mostrarEstadisticas
                mostrarEstadisticas()
                pausar()
            elif opcion_int == 0:
                break
            else:
                print(f"{RED}⚠️ Opción inválida{RESET}")
                pausar()


def menu_usuarios():
    limpiar()
    titulo("👤 LISTADO DE USUARIOS")
    mostrarUsuarios()
    pausar()


menu_principal()
