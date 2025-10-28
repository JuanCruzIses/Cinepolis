from db import listaPeliculas
from db import listaResenas
from db import listaUsuarios
import crudPeliculas

# test DB
def test_lista_no_vacia():
    assert len(listaPeliculas) > 0

def test_claves_peliculas():
    for pelicula in listaPeliculas:
        assert "id" in pelicula
        assert "titulo" in pelicula
        assert "estreno" in pelicula
        assert "director" in pelicula
        assert "generos" in pelicula
        assert "sinopsis" in pelicula
        assert "poster" in pelicula

def test_ids_unicos():
    ids = []
    for pelicula in listaPeliculas:
        ids.append(pelicula["id"])
    assert len(ids) == len(set(ids)) #set lo usamos para ver que no esten repetidos

def test_sagas():
    titulos = [p["titulo"].lower() for p in listaPeliculas]
    assert len(titulos) != len(set(titulos)) #set lo usamos para ver que esten repetidos los titulos

def test_estreno_valido():
    for pelicula in listaPeliculas:
        assert pelicula["estreno"] > 1800

def test_puntuacion_valida():
    for r in listaResenas:
        assert 0 <= r["puntuacion"] <= 10

def test_reseñas_referencian_peliculas_validas():
    titulos = [p["titulo"].lower() for p in listaPeliculas]
    for r in listaResenas:
        assert r["pelicula"].lower() in titulos

def test_reseñas_referencian_usuarios_validos():
    usuarios = [u["usuario"].lower() for u in listaUsuarios]
    for r in listaResenas:
        assert r["usuario"].lower() in usuarios

def test_emails_unicos():
    emails = [u["email"].lower() for u in listaUsuarios]
    assert len(emails) == len(set(emails)) #set lo usamos para ver que no esten repetidos

def test_roles_validos():
    roles_validos = ["admin", "user"]
    for u in listaUsuarios:
        assert u["rol"].lower() in roles_validos


# test CRUD Películas
def test_lista_peliculas_valida():
    for p in listaPeliculas:
        assert "id" in p
        assert "titulo" in p
        assert "estreno" in p
        assert "director" in p

def test_funciones_crud_existen(): # el dir lo usamos para apuntar al archivo de crudPeliculas para ver si las funciones esas estan
    assert "crearPelicula" in dir(crudPeliculas)
    assert "editarPelicula" in dir(crudPeliculas)
    assert "eliminarPelicula" in dir(crudPeliculas)
    assert "mostrarPeliculas" in dir(crudPeliculas)

#test CRUD Reseñas
def test_lista_resenas_valida():
    for r in listaResenas:
        assert "id" in r
        assert "usuario" in r
        assert "pelicula" in r
        assert "puntuacion" in r
        assert "titulo" in r
        assert "comentario" in r

#test CRUD Usuarios
def test_lista_usuarios_valida():
    for u in listaUsuarios:
        assert "id" in u
        assert "usuario" in u
        assert "email" in u
        assert "clave" in u
        assert "rol" in u



