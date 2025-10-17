#Imports de librerias
import os

#Imports de funciones del programa
from crudPeliculas import crudPeliculas
from crudUsuarios import crudUsuarios
from crudResenas import crudResenas

# Menu Principal
def menuPrincipal():
    usuario = 0
    print("----- Sistema de Gestion -----")
    print("1. Peliculas \n2. Usuarios \n3. Reseñas \n4. Finalizar programa")
    opcion = int(input("Seleccione la opcion: "))
    print(usuario)
    while opcion != 4:
        if usuario != 0 and usuario != None:
            print(f'Usuario: {usuario["usuario"]} \nReseñas: {usuario["cantidad_reseñas"]}')
        if opcion == 1:
            crudPeliculas(usuario)
        elif opcion == 2:
            usuario = crudUsuarios(usuario)
        elif opcion == 3:
            crudResenas(usuario)
        else:
            print("Opcion invalida")
        
        if usuario != 0 and usuario != None:
            print(f'Usuario: {usuario["usuario"]} \nReseñas: {usuario["cantidad_reseñas"]}')
        print("\n1. Peliculas \n2. Usuarios \n3. Reseñas \n4. Finalizar programa")
        opcion = int(input("Seleccione la opcion: "))
        print("")


# Ejecutar menu principal
menuPrincipal()