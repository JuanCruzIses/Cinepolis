# 🎬 Cinépolis - Sistema de Películas

Un sistema para gestionar películas, ver reseñas y comentar sobre tus películas favoritas.

## ▶️ Cómo Ejecutar
python main.py

## 📖 Guía de Uso Paso a Paso

### 1️⃣ Pantalla de Inicio

Cuando ejecutes el programa verás el **menú principal** con varias opciones:

```
========== MENÚ PRINCIPAL ==========
1. Ver Películas
2. Buscar Película
3. Ver Reseñas
4. Iniciar Sesión
5. Salir
```

### 2️⃣ Ver Películas

Selecciona la opción **1** para ver el listado completo de todas las películas disponibles.

- Muestra: Título, Año, Director y Género
- Puedes navegar por la lista

### 3️⃣ Buscar una Película

Selecciona la opción **2** para buscar:

1. Ingresa el nombre de la película (ej: "Harry Potter", "El Padrino")
2. El sistema buscará coincidencias
3. Te mostrará las películas encontradas con números
4. Elige el número de la película que deseas ver
5. Verás la información completa: sinopsis, director, año, etc.

### 4️⃣ Ver Reseñas

Selecciona la opción **3**:

1. Ingresa el nombre de la película
2. Se mostrarán todas las reseñas de esa película
3. Verás quién escribió la reseña y qué opinó

### 5️⃣ Iniciar Sesión

Selecciona la opción **4** para crear tu cuenta:

1. Ingresa un usuario
2. Ingresa una contraseña
3. Se guardará tu información

**Después de iniciar sesión podrás:**
- ✅ Crear reseñas de películas
- ✅ Ver tus reseñas guardadas
- ✅ Acceder a más funciones

### 6️⃣ Crear una Reseña (Solo si iniciaste sesión)

Una vez logueado:

1. Busca una película
2. Selecciona la opción para crear reseña
3. Escribe tu opinión
4. Se guardará automáticamente

### 7️⃣ Salir

Selecciona la opción **5** para cerrar el programa.

## 🗂️ Estructura de Archivos

```
├── main.py               # Programa principal
├── crudPeliculas.py      # Gestión de películas
├── crudResenas.py        # Gestión de reseñas
├── crudUsuarios.py       # Gestión de usuarios
├── funcionesFile.py      # Manejo de archivos
├── db.py                 # Base de datos de películas
└── db/                   # Carpeta de datos
    ├── usuarios.json     # Tus cuentas
    ├── peliculas.json    # Películas disponibles
    └── resenas.json      # Reseñas guardadas
```

## 💡 Tips

- Las búsquedas funcionan con palabras sueltas (busca "Harry" para encontrar todas las películas de Harry Potter)
- Puedes dejar espacios en blanco sin problema
- Las contraseñas se guardan para iniciar sesión después
- Tu usuario queda recordado en el sistema

## 📌 Requisitos

- Python 3.7 o superior
- Sin dependencias externas necesarias

---

¡Disfruta viendo películas! 🎥
