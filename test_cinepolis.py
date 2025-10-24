from db import listaPeliculas
from db import listaResenas
from db import listaUsuarios

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
    assert len(ids) == len(set(ids))

def test_estreno_valido():
    for pelicula in listaPeliculas:
        assert pelicula["estreno"] > 1800

# test CRUD Películas
def test_lista_peliculas_valida():
    for p in listaPeliculas:
        assert "id" in p
        assert "titulo" in p
        assert "estreno" in p
        assert "director" in p

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
        assert "contraseña" in u
        assert "rol" in u



