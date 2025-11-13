from db import listaPeliculas
from db import listaResenas
from db import listaUsuarios
import crudPeliculas
import crudResenas
import crudUsuarios


# TEST BD

    # Verifica que haya películas cargadas
def test_lista_no_vacia():
    assert len(listaPeliculas) > 0


    # Verifica que cada película tenga las claves necesarias
def test_claves_peliculas():
    for pelicula in listaPeliculas:
        assert "id" in pelicula
        assert "titulo" in pelicula
        assert "estreno" in pelicula
        assert "director" in pelicula
        assert "generos" in pelicula
        assert "sinopsis" in pelicula
        assert "poster" in pelicula


    # Los IDs de películas no deben repetirse
def test_ids_unicos():
    ids = []
    for pelicula in listaPeliculas:
        ids.append(pelicula["id"])
    assert len(ids) == len(set(ids))

# corregir sagas
""" def test_sagas():
    # Debe haber al menos una saga (título repetido)
    titulos = [p["titulo"].lower() for p in listaPeliculas]
    assert len(titulos) != len(set(titulos)) 
"""


    # El año de estreno debe ser mayor a 1800
def test_estreno_valido():
    for pelicula in listaPeliculas:
        assert pelicula["estreno"] > 1800


# TEST DE RESEÑAS

    # Verifica que cada reseña tenga todas las claves necesarias
def test_lista_resenas_valida():
    for r in listaResenas:
        assert "id" in r
        assert "usuario" in r
        assert "pelicula" in r
        assert "puntuacion" in r
        assert "titulo" in r
        assert "comentario" in r


    # Las puntuaciones deben estar entre 0 y 10
def test_puntuacion_valida():
    for r in listaResenas:
        assert 0 <= r["puntuacion"] <= 10


    # Cada reseña debe estar asociada a una película existente
def test_reseñas_referencian_peliculas_validas():
    titulos = [p["titulo"].lower() for p in listaPeliculas]
    for r in listaResenas:
        assert r["pelicula"].lower() in titulos


    # Cada reseña debe pertenecer a un usuario existente
def test_reseñas_referencian_usuarios_validos():
    usuarios = [u["usuario"].lower() for u in listaUsuarios]
    for r in listaResenas:
        assert r["usuario"].lower() in usuarios



# TEST DE USUARIOS

    # Verifica que cada usuario tenga las claves necesarias
def test_lista_usuarios_valida():
    for u in listaUsuarios:
        assert "id" in u
        assert "usuario" in u
        assert "email" in u
        assert "clave" in u
        assert "rol" in u


    # Los emails no deben repetirse
def test_emails_unicos():
    emails = [u["email"].lower() for u in listaUsuarios]
    assert len(emails) == len(set(emails))


    # Los roles deben ser admin o user
def test_roles_validos():
    roles_validos = ["admin", "user"]
    for u in listaUsuarios:
        assert u["rol"].lower() in roles_validos



# TEST CRUD 

    # Verifica que las funciones CRUD de películas existan
def test_funciones_crud_peliculas_existen():
    assert "crearPelicula" in dir(crudPeliculas)
    assert "editarPelicula" in dir(crudPeliculas)
    assert "eliminarPelicula" in dir(crudPeliculas)
    assert "mostrarPeliculas" in dir(crudPeliculas)


    # Verifica que las funciones CRUD de reseñas existan
def test_funciones_crud_resenas_existen():
    assert "crearResenas" in dir(crudResenas)
    assert "mostrarResenas" in dir(crudResenas)
    assert "crudResenas" in dir(crudResenas)
    assert "mostrarEstadisticas" in dir(crudResenas)


    # Verifica que las funciones CRUD de usuarios existan
def test_funciones_crud_usuarios_existen():
    assert "crearUsuario" in dir(crudUsuarios)
    assert "iniciarSesion" in dir(crudUsuarios)
    assert "editarUsuario" in dir(crudUsuarios)
    assert "eliminarUsuario" in dir(crudUsuarios)
    assert "cerrarSesion" in dir(crudUsuarios)
    assert "mostrarUsuarios" in dir(crudUsuarios)
    assert "crudUsuarios" in dir(crudUsuarios)
