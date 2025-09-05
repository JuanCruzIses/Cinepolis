#Listado de 100 peliculas (id, título, estreno, director, géneros, poster, sinopsis)
listaPeliculas = [
    {
        "id": 1,
        "titulo": "El Padrino",
        "estreno": 1972,
        "director": "Francis Ford Coppola",
        "generos": ["Crimen", "Drama"],
        "poster": "",
        "sinopsis": (
            "La historia de la familia Corleone, una de las más poderosas de la mafia italiana en Nueva York. "
            "Vito Corleone, el patriarca, intenta mantener a salvo a su familia en un mundo de traiciones, poder y violencia. "
            "Cuando su vida es amenazada, su hijo Michael se ve obligado a tomar el control del imperio familiar. "
            "La película explora la corrupción, la lealtad y el precio del poder en una saga épica."
        )
    },
    {
        "id": 2,
        "titulo": "Forrest Gump",
        "estreno": 1994,
        "director": "Robert Zemeckis",
        "generos": ["Drama", "Romance"],
        "poster": "",
        "sinopsis": (
            "Forrest Gump, un hombre con un bajo coeficiente intelectual pero con una bondad infinita, narra su extraordinaria vida. "
            "Desde su infancia en Alabama hasta convertirse en testigo y protagonista de momentos clave de la historia de Estados Unidos. "
            "Su amor incondicional por Jenny, su amiga de la infancia, guía gran parte de su vida. "
            "La película combina humor, ternura y reflexión sobre el destino y la simplicidad del corazón humano."
        )
    },
    {
        "id": 3,
        "titulo": "Parasite",
        "estreno": 2019,
        "director": "Bong Joon-ho",
        "generos": ["Drama", "Thriller"],
        "poster": "",
        "sinopsis": (
            "La familia Kim, desempleada y pobre, encuentra la manera de infiltrarse en la vida de la rica familia Park. "
            "A medida que cada miembro consigue un trabajo dentro de la mansión, las diferencias de clase se vuelven más evidentes. "
            "Lo que empieza como un ingenioso plan se transforma en una oscura lucha de poder y supervivencia. "
            "Una crítica feroz a la desigualdad social con tintes de comedia negra y thriller impactante."
        )
    },
    {
        "id": 4,
        "titulo": "Inception",
        "estreno": 2010,
        "director": "Christopher Nolan",
        "generos": ["Ciencia ficción", "Acción", "Thriller"],
        "poster": "",
        "sinopsis": (
            "Dom Cobb es un ladrón especializado en infiltrarse en los sueños para robar secretos de la mente inconsciente. "
            "Su habilidad lo convierte en un fugitivo, pero también le ofrece la oportunidad de redención: implantar una idea en lugar de robarla. "
            "Con su equipo, debe realizar un complejo atraco onírico que desafía la lógica de la realidad. "
            "Una exploración de la mente, los recuerdos y la delgada línea entre los sueños y la vida real."
        )
    },
    {
        "id": 5,
        "titulo": "Amélie",
        "estreno": 2001,
        "director": "Jean-Pierre Jeunet",
        "generos": ["Comedia romántica", "Drama"],
        "poster": "",
        "sinopsis": (
            "Amélie Poulain es una joven parisina con una imaginación desbordante y un gran corazón. "
            "Descubre la alegría de cambiar la vida de los demás a través de pequeños gestos anónimos. "
            "Mientras transforma su barrio con actos de bondad, lucha con su propia timidez y busca el amor verdadero. "
            "Una oda a la magia de lo cotidiano, al optimismo y al poder de las pequeñas cosas."
        )
    },
    {
        "id": 6,
        "titulo": "Ciudad de Dios",
        "estreno": 2002,
        "director": "Fernando Meirelles, Kátia Lund",
        "generos": ["Crimen", "Drama"],
        "poster": "",
        "sinopsis": (
            "Basada en hechos reales, narra la vida en una favela de Río de Janeiro desde finales de los estrenos 60 hasta los 80. "
            "La historia sigue a Buscapé, un joven que sueña con ser fotógrafo, y a Zé Pequeño, un niño que se convierte en uno de los criminales más temidos. "
            "El relato muestra cómo la violencia, la droga y la pobreza marcan a generaciones enteras. "
            "Un retrato descarnado y vibrante de la desigualdad social en Brasil."
        )
    },
    {
        "id": 7,
        "titulo": "La lista de Schindler",
        "estreno": 1993,
        "director": "Steven Spielberg",
        "generos": ["Drama", "Historia", "Biografía"],
        "poster": "",
        "sinopsis": (
            "Oskar Schindler, un empresario alemán, se convierte en un inesperado héroe durante el Holocausto. "
            "Al principio motivado por intereses económicos, empieza a emplear a judíos en su fábrica para salvarlos de la deportación. "
            "A medida que la tragedia avanza, su empresa se transforma en un refugio de vida. "
            "Una conmovedora historia de redención y humanidad en medio de la barbarie."
        )
    },
    {
        "id": 8,
        "titulo": "Pulp Fiction",
        "estreno": 1994,
        "director": "Quentin Tarantino",
        "generos": ["Crimen", "Drama", "Comedia negra"],
        "poster": "",
        "sinopsis": (
            "Una narrativa no lineal entrelaza las vidas de gánsteres, boxeadores, criminales menores y una misteriosa maleta. "
            "Vincent Vega y Jules Winnfield son dos asesinos a sueldo que discuten sobre la vida mientras cumplen violentas misiones. "
            "La historia incluye un boxeador en fuga y una sobredosis accidental que cambia destinos. "
            "Con diálogos memorables y humor negro, redefine el cine de los 90 con estilo y violencia estilizada."
        )
    },
    {
        "id": 9,
        "titulo": "El viaje de Chihiro",
        "estreno": 2001,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Chihiro, una niña de 10 estrenos, se encuentra atrapada en un mundo mágico tras mudarse con sus padres. "
            "Sus padres son transformados en cerdos y ella debe trabajar en un balneario espiritual para encontrar la forma de liberarlos. "
            "A lo largo de su viaje, descubre el valor, la amistad y la resiliencia. "
            "Una obra maestra de Studio Ghibli que combina fantasía deslumbrante con profundas lecciones de vida."
        )
    },
    {
        "id": 10,
        "titulo": "Gladiador",
        "estreno": 2000,
        "director": "Ridley Scott",
        "generos": ["Acción", "Drama", "Historia"],
        "poster": "",
        "sinopsis": (
            "Máximo Décimo Meridio, un leal general romano, es traicionado por Cómodo, el ambicioso hijo del emperador. "
            "Tras perder a su familia y su libertad, es condenado a luchar como gladiador. "
            "Su búsqueda de justicia y venganza lo convierte en una figura legendaria dentro de la arena. "
            "Un épico relato de honor, traición y redención en la antigua Roma."
        )
    },
    {
        "id": 11,
        "titulo": "Titanic",
        "estreno": 1997,
        "director": "James Cameron",
        "generos": ["Romance", "Drama"],
        "poster": "",
        "sinopsis": (
            "La historia de amor entre Jack y Rose a bordo del lujoso Titanic, el trasatlántico más grande de su época. "
            "Ella, una joven de clase alta atrapada en un compromiso sin amor, encuentra en Jack, un humilde artista, la libertad que anhela. "
            "Su romance florece mientras el barco navega hacia la tragedia inevitable. "
            "Un relato épico de amor, destino y el choque entre clases sociales."
        )
    },
    {
        "id": 12,
        "titulo": "Casablanca",
        "estreno": 1942,
        "director": "Michael Curtiz",
        "generos": ["Romance", "Drama", "Guerra"],
        "poster": "",
        "sinopsis": (
            "Rick Blaine, dueño de un café en Casablanca, se reencuentra con Ilsa, el amor de su vida, en plena Segunda Guerra Mundial. "
            "Ella llega acompañada de su esposo, un líder de la resistencia, lo que obliga a Rick a enfrentar su doloroso pasado. "
            "El destino de los personajes se mezcla con intrigas políticas y pasiones inconclusas. "
            "Un clásico eterno sobre sacrificio, amor perdido y lealtad en tiempos de guerra."
        )
    },
    {
        "id": 13,
        "titulo": "The Dark Knight",
        "estreno": 2008,
        "director": "Christopher Nolan",
        "generos": ["Acción", "Crimen", "Drama"],
        "poster": "",
        "sinopsis": (
            "Batman enfrenta a su mayor enemigo: el Joker, un criminal que busca sumir a Gotham en el caos absoluto. "
            "Con la ayuda del fiscal Harvey Dent y el comisionado Gordon, intenta detener la ola de violencia que amenaza con destruir la ciudad. "
            "La película explora la delgada línea entre justicia y venganza, y los sacrificios necesarios para proteger a los inocentes. "
            "Una obra intensa, sombría y filosófica que redefine el cine de superhéroes."
        )
    },
    {
        "id": 14,
        "titulo": "El laberinto del fauno",
        "estreno": 2006,
        "director": "Guillermo del Toro",
        "generos": ["Fantasía", "Drama", "Guerra"],
        "poster": "",
        "sinopsis": (
            "En la España franquista de 1944, Ofelia, una niña amante de los cuentos de hadas, descubre un misterioso fauno en un laberinto cercano. "
            "El ser le asigna tres pruebas para demostrar que es la reencarnación de una princesa perdida. "
            "Mientras tanto, la brutalidad del capitán Vidal, su padrastro, convierte su vida en una pesadilla. "
            "Una fábula oscura que mezcla la crudeza histórica con la fantasía mágica."
        )
    },
    {
        "id": 15,
        "titulo": "La La Land",
        "estreno": 2016,
        "director": "Damien Chazelle",
        "generos": ["Musical", "Romance", "Drama"],
        "poster": "",
        "sinopsis": (
            "Mia, una aspirante a actriz, y Sebastian, un pianista de jazz, luchan por cumplir sus sueños en Los Ángeles. "
            "Su relación apasionada se ve puesta a prueba cuando sus carreras los llevan por caminos distintos. "
            "El film combina números musicales vibrantes con una historia de amor realista y agridulce. "
            "Una carta de amor a los soñadores y a la magia del cine clásico."
        )
    },
    {
        "id": 16,
        "titulo": "12 estrenos de esclavitud",
        "estreno": 2013,
        "director": "Steve McQueen",
        "generos": ["Drama", "Historia", "Biografía"],
        "poster": "",
        "sinopsis": (
            "Solomon Northup, un hombre negro libre en Nueva York, es secuestrado y vendido como esclavo en el sur de Estados Unidos. "
            "Durante doce estrenos soporta abusos, humillaciones y trabajos forzados mientras lucha por sobrevivir y recuperar su libertad. "
            "Su historia refleja la brutalidad del sistema esclavista y la resiliencia del espíritu humano. "
            "Una obra conmovedora que denuncia la injusticia histórica con crudeza y esperanza."
        )
    },
    {
        "id": 17,
        "titulo": "Interstellar",
        "estreno": 2014,
        "director": "Christopher Nolan",
        "generos": ["Ciencia ficción", "Drama", "Aventura"],
        "poster": "",
        "sinopsis": (
            "En un futuro distópico donde la Tierra agoniza, un grupo de astronautas viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad. "
            "Cooper, piloto y padre, debe enfrentarse a la distancia con su hija mientras el tiempo en el espacio transcurre de manera diferente. "
            "La película explora la relatividad, la esperanza y el poder del amor como fuerza trascendental. "
            "Una epopeya científica y emocional de proporciones cósmicas."
        )
    },
    {
        "id": 18,
        "titulo": "El silencio de los inocentes",
        "estreno": 1991,
        "director": "Jonathan Demme",
        "generos": ["Thriller", "Crimen", "Terror psicológico"],
        "poster": "",
        "sinopsis": (
            "Clarice Starling, una joven agente del FBI, busca atrapar a un asesino serial apodado Buffalo Bill. "
            "Para lograrlo, debe recurrir a Hannibal Lecter, un brillante psiquiatra encarcelado por canibalismo. "
            "La tensa relación entre ambos se convierte en un duelo psicológico inquietante. "
            "Un thriller magistral que combina terror, inteligencia y suspenso."
        )
    },
    {
        "id": 19,
        "titulo": "Matrix",
        "estreno": 1999,
        "director": "Lana y Lilly Wachowski",
        "generos": ["Ciencia ficción", "Acción"],
        "poster": "",
        "sinopsis": (
            "Neo, un joven programador, descubre que la realidad que conoce es una simulación creada por máquinas para controlar a la humanidad. "
            "Con la ayuda de Morfeo y Trinity, se une a la rebelión contra el sistema artificial. "
            "Entre combates espectaculares y reflexiones filosóficas, debe aceptar su destino como 'El Elegido'. "
            "Una obra revolucionaria que redefinió el cine de ciencia ficción."
        )
    },
    {
        "id": 20,
        "titulo": "La vida es bella",
        "estreno": 1997,
        "director": "Roberto Benigni",
        "generos": ["Drama", "Romance", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Guido, un hombre carismático y soñador, conquista a Dora y juntos forman una familia. "
            "Cuando son deportados a un campo de concentración, Guido utiliza su ingenio para convencer a su hijo de que todo es un juego. "
            "Su sacrificio y amor incondicional se convierten en un escudo frente al horror. "
            "Una película que mezcla ternura y tragedia con un mensaje de esperanza inolvidable."
        )
    },
        {
        "id": 21,
        "titulo": "El club de la pelea",
        "estreno": 1999,
        "director": "David Fincher",
        "generos": ["Drama", "Thriller", "Psicológico"],
        "poster": "",
        "sinopsis": (
            "Un hombre insomne y desencantado de la sociedad moderna encuentra en Tyler Durden un carismático vendedor de jabón. "
            "Juntos fundan un club secreto donde hombres frustrados liberan su ira en brutales peleas. "
            "Lo que empieza como un desahogo se convierte en un movimiento anárquico contra el consumismo. "
            "Un relato provocador sobre identidad, alienación y la violencia como catarsis."
        )
    },
    {
        "id": 22,
        "titulo": "El bueno, el malo y el feo",
        "estreno": 1966,
        "director": "Sergio Leone",
        "generos": ["Western", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Tres forajidos, cada uno con motivaciones distintas, compiten por encontrar un tesoro enterrado en medio de la guerra civil estadounidense. "
            "La tensión entre ellos se incrementa en un duelo legendario en un cementerio desierto. "
            "Con una dirección impecable y música inolvidable de Ennio Morricone, redefine el spaghetti western. "
            "Un clásico del cine que mezcla humor, violencia y épica."
        )
    },
    {
        "id": 23,
        "titulo": "Coco",
        "estreno": 2017,
        "director": "Lee Unkrich, Adrian Molina",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Miguel, un niño mexicano apasionado por la música, sueña con ser guitarrista pese a la prohibición de su familia. "
            "Durante el Día de Muertos, accidentalmente cruza al mundo de los muertos donde descubre la historia de sus ancestros. "
            "Con ayuda de Héctor, emprende una aventura para encontrar su lugar en la tradición familiar. "
            "Un viaje emotivo sobre la memoria, la identidad y el poder de la música."
        )
    },
    {
        "id": 24,
        "titulo": "Joker",
        "estreno": 2019,
        "director": "Todd Phillips",
        "generos": ["Drama", "Thriller", "Psicológico"],
        "poster": "",
        "sinopsis": (
            "Arthur Fleck, un hombre marginado con problemas mentales, sobrevive trabajando como payaso en una sociedad que lo rechaza. "
            "Su transformación en el icónico villano Joker se desarrolla entre abusos, humillaciones y una búsqueda desesperada de reconocimiento. "
            "El film retrata la fragilidad de la mente humana y las fallas del sistema social. "
            "Una historia oscura, intensa y profundamente perturbadora."
        )
    },
    {
        "id": 25,
        "titulo": "Avatar",
        "estreno": 2009,
        "director": "James Cameron",
        "generos": ["Ciencia ficción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Jake Sully, un exmarine parapléjico, es enviado al planeta Pandora como parte de un proyecto militar y científico. "
            "A través de un avatar, entra en contacto con los Na'vi, una civilización en armonía con la naturaleza. "
            "Dividido entre la obediencia militar y el amor por Neytiri, debe decidir de qué lado estar. "
            "Un espectáculo visual revolucionario sobre ecología, colonización y conexión espiritual."
        )
    },
    {
        "id": 26,
        "titulo": "Whiplash",
        "estreno": 2014,
        "director": "Damien Chazelle",
        "generos": ["Drama", "Música"],
        "poster": "",
        "sinopsis": (
            "Andrew, un joven baterista de jazz, ingresa a un prestigioso conservatorio bajo la tutela de Fletcher, un maestro implacable y abusivo. "
            "La relación entre ambos se convierte en una batalla psicológica donde el perfeccionismo y el sacrificio lo son todo. "
            "El camino hacia la grandeza exige dolor, disciplina y obsesión. "
            "Un retrato intenso del precio del arte y la ambición."
        )
    },
    {
        "id": 27,
        "titulo": "El resplandor",
        "estreno": 1980,
        "director": "Stanley Kubrick",
        "generos": ["Terror", "Psicológico"],
        "poster": "",
        "sinopsis": (
            "Jack Torrance acepta un trabajo como cuidador de invierno en un aislado hotel junto a su esposa e hijo. "
            "A medida que la soledad y las fuerzas sobrenaturales lo consumen, cae en una espiral de locura violenta. "
            "El pequeño Danny, dotado de un don psíquico, percibe el horror antes que nadie. "
            "Una obra maestra del terror psicológico basada en la novela de Stephen King."
        )
    },
    {
        "id": 28,
        "titulo": "Amadeus",
        "estreno": 1984,
        "director": "Milos Forman",
        "generos": ["Biografía", "Drama", "Música"],
        "poster": "",
        "sinopsis": (
            "La vida y obra de Wolfgang Amadeus Mozart narrada desde la perspectiva de Antonio Salieri, un compositor envidioso de su talento. "
            "Mientras Mozart brilla con su genialidad desbordante, Salieri se consume en celos y resentimiento. "
            "El enfrentamiento entre ambos se convierte en una metáfora de la mediocridad frente al genio. "
            "Un film grandioso sobre arte, pasión y obsesión."
        )
    },
    {
        "id": 29,
        "titulo": "Los siete samuráis",
        "estreno": 1954,
        "director": "Akira Kurosawa",
        "generos": ["Acción", "Drama", "Épico"],
        "poster": "",
        "sinopsis": (
            "Un grupo de campesinos contrata a siete samuráis para defender su aldea de los ataques de bandidos. "
            "A lo largo de la preparación, guerreros y campesinos establecen lazos de respeto y sacrificio. "
            "La batalla final se convierte en una lección de honor y humanidad. "
            "Una de las películas más influyentes de la historia del cine."
        )
    },
    {
        "id": 30,
        "titulo": "Her",
        "estreno": 2013,
        "director": "Spike Jonze",
        "generos": ["Ciencia ficción", "Romance", "Drama"],
        "poster": "",
        "sinopsis": (
            "Theodore, un hombre solitario, desarrolla una relación con un sistema operativo inteligente llamado Samantha. "
            "Lo que comienza como un vínculo práctico evoluciona en una profunda conexión emocional. "
            "La historia cuestiona los límites entre amor, tecnología y soledad. "
            "Un retrato poético de las relaciones en la era digital."
        )
    },
    {
        "id": 31,
        "titulo": "Toy Story",
        "estreno": 1995,
        "director": "John Lasseter",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Woody, un vaquero de juguete, ve peligrar su lugar como el favorito de Andy cuando aparece Buzz Lightyear, un moderno astronauta. "
            "Ambos deben superar sus diferencias cuando se enfrentan al peligro de perderse para siempre. "
            "La película explora la amistad, la lealtad y el miedo al abandono. "
            "La primera cinta animada por computadora que revolucionó el cine."
        )
    },
    {
        "id": 32,
        "titulo": "Los Increíbles",
        "estreno": 2004,
        "director": "Brad Bird",
        "generos": ["Animación", "Acción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Una familia de superhéroes retirados trata de llevar una vida normal bajo el anonimato. "
            "Cuando un nuevo villano amenaza el mundo, deben unirse y volver a la acción. "
            "La historia combina humor, acción y una exploración del valor de la familia. "
            "Un clásico de Pixar que mezcla lo épico con lo íntimo."
        )
    },
    {
        "id": 33,
        "titulo": "Shrek",
        "estreno": 2001,
        "director": "Andrew Adamson, Vicky Jenson",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Shrek, un ogro solitario, emprende un viaje para rescatar a la princesa Fiona y recuperar la paz en su pantano. "
            "Acompañado de su parlanchín amigo Burro, descubre que el amor puede encontrarse en lugares inesperados. "
            "La película parodia los cuentos de hadas tradicionales con ingenio y humor. "
            "Una historia entrañable sobre la aceptación y la verdadera belleza."
        )
    },
    {
        "id": 34,
        "titulo": "Up",
        "estreno": 2009,
        "director": "Pete Docter",
        "generos": ["Animación", "Aventura", "Drama"],
        "poster": "",
        "sinopsis": (
            "Carl, un viudo anciano, cumple el sueño que compartía con su esposa: viajar a Sudamérica. "
            "Ata miles de globos a su casa y emprende el viaje acompañado inesperadamente por un niño explorador. "
            "En su camino descubren amistades improbables y aventuras memorables. "
            "Una película emotiva sobre los sueños, la pérdida y la esperanza."
        )
    },
    {
        "id": 35,
        "titulo": "Wall-E",
        "estreno": 2008,
        "director": "Andrew Stanton",
        "generos": ["Animación", "Ciencia ficción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "En un futuro donde la Tierra ha sido abandonada por la humanidad, un pequeño robot llamado Wall-E sigue limpiando la basura. "
            "Su vida cambia al conocer a EVA, una sonda enviada desde el espacio. "
            "Juntos inician una aventura que puede devolver la esperanza al planeta. "
            "Una historia poética sobre amor, ecología y humanidad."
        )
    },
    {
        "id": 36,
        "titulo": "Buscando a Nemo",
        "estreno": 2003,
        "director": "Andrew Stanton, Lee Unkrich",
        "generos": ["Animación", "Aventura", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Cuando el pequeño pez Nemo es capturado por un buzo, su padre Marlin emprende un viaje épico para rescatarlo. "
            "Acompañado por la olvidadiza Dory, atraviesa océanos llenos de peligros y personajes pintorescos. "
            "El viaje se convierte en una lección de confianza y amor paternal. "
            "Un clásico de Pixar que celebra la aventura y la familia."
        )
    },
    {
        "id": 37,
        "titulo": "Soul",
        "estreno": 2020,
        "director": "Pete Docter, Kemp Powers",
        "generos": ["Animación", "Drama", "Fantasía"],
        "poster": "",
        "sinopsis": (
            "Joe, un profesor de música frustrado, muere en un accidente justo antes de cumplir su sueño de ser jazzista. "
            "En el Más Allá, intenta regresar a la Tierra con la ayuda de un alma joven llamada 22. "
            "Juntos descubren qué significa realmente vivir. "
            "Una reflexión emotiva sobre el propósito, la pasión y la vida cotidiana."
        )
    },
    {
        "id": 38,
        "titulo": "El rey león",
        "estreno": 1994,
        "director": "Roger Allers, Rob Minkoff",
        "generos": ["Animación", "Drama", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Simba, un joven león heredero al trono, huye tras la muerte de su padre provocada por la traición de su tío Scar. "
            "En el exilio, crece con nuevos amigos hasta que debe regresar a reclamar su lugar legítimo. "
            "La película explora el ciclo de la vida, la pérdida y la responsabilidad. "
            "Un hito de Disney con música inolvidable."
        )
    },
    {
        "id": 39,
        "titulo": "Frozen",
        "estreno": 2013,
        "director": "Chris Buck, Jennifer Lee",
        "generos": ["Animación", "Fantasía", "Musical"],
        "poster": "",
        "sinopsis": (
            "Anna emprende un viaje junto a Kristoff y Olaf para encontrar a su hermana Elsa, cuyos poderes de hielo han sumido al reino en un invierno eterno. "
            "La historia resalta el amor fraternal y la aceptación de uno mismo como fuerzas transformadoras. "
            "Con canciones inolvidables, redefinió el género de princesas Disney. "
            "Una aventura mágica sobre coraje y lazos familiares."
        )
    },
    {
        "id": 40,
        "titulo": "Moana",
        "estreno": 2016,
        "director": "Ron Clements, John Musker",
        "generos": ["Animación", "Aventura", "Musical"],
        "poster": "",
        "sinopsis": (
            "Moana, la hija del jefe de una isla polinesia, emprende un viaje para salvar a su pueblo. "
            "Acompañada por el semidiós Maui, se enfrenta a monstruos marinos y desafíos legendarios. "
            "El viaje la lleva a descubrir su verdadera identidad como líder y exploradora. "
            "Una historia vibrante sobre el coraje y la conexión con la naturaleza."
        )
    },
    {
        "id": 41,
        "titulo": "Inside Out",
        "estreno": 2015,
        "director": "Pete Docter",
        "generos": ["Animación", "Drama", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Riley, una niña de 11 estrenos, enfrenta un gran cambio cuando su familia se muda a otra ciudad. "
            "Sus emociones —Alegría, Tristeza, Furia, Temor y Desagrado— deben aprender a trabajar juntas. "
            "La aventura interna refleja cómo la tristeza puede ser tan valiosa como la felicidad. "
            "Una mirada original a la psicología emocional con ternura y humor."
        )
    },
    {
        "id": 42,
        "titulo": "Ratatouille",
        "estreno": 2007,
        "director": "Brad Bird, Jan Pinkava",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Remy, una rata con un talento extraordinario para la cocina, sueña con ser chef en París. "
            "Aliado con Linguini, un joven torpe, logra conquistar paladares y demostrar que cualquiera puede cocinar. "
            "La película celebra la pasión, la creatividad y la perseverancia. "
            "Un festín visual y narrativo de Pixar."
        )
    },
    {
        "id": 43,
        "titulo": "Zootopia",
        "estreno": 2016,
        "director": "Byron Howard, Rich Moore",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Judy Hopps, una coneja policía novata, une fuerzas con el zorro estafador Nick Wilde para resolver un misterio. "
            "Juntos descubren una conspiración que amenaza la convivencia entre depredadores y presas. "
            "La película aborda prejuicios y discriminación a través de un mundo animal vibrante. "
            "Un relato ingenioso y actual sobre diversidad y tolerancia."
        )
    },
    {
        "id": 44,
        "titulo": "Los juegos del hambre",
        "estreno": 2012,
        "director": "Gary Ross",
        "generos": ["Ciencia ficción", "Acción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "En un futuro distópico, los distritos de Panem deben enviar tributos para luchar a muerte en un cruel espectáculo televisado. "
            "Katniss Everdeen se ofrece voluntaria para salvar a su hermana y se convierte en símbolo de resistencia. "
            "La historia combina acción trepidante con crítica social y política. "
            "Un fenómeno cultural que redefinió la ciencia ficción juvenil."
        )
    },
    {
        "id": 45,
        "titulo": "Harry Potter y la piedra filosofal",
        "estreno": 2001,
        "director": "Chris Columbus",
        "generos": ["Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Harry Potter, un niño huérfano, descubre el día de su cumpleestrenos que es un mago. "
            "Al ingresar en Hogwarts, conoce a Ron y Hermione y comienza su viaje en el mundo mágico. "
            "La película introduce la lucha contra Voldemort, un villano que amenaza con volver. "
            "Una puerta de entrada al universo mágico más famoso de la literatura moderna."
        )
    },
    {
        "id": 46,
        "titulo": "Harry Potter y las reliquias de la muerte (Parte 2)",
        "estreno": 2011,
        "director": "David Yates",
        "generos": ["Fantasía", "Aventura", "Acción"],
        "poster": "",
        "sinopsis": (
            "La batalla final entre Harry y Voldemort alcanza su clímax en Hogwarts. "
            "Los personajes enfrentan pérdidas irreparables y pruebas de valor definitivo. "
            "El sacrificio, la amistad y el amor se revelan como las mayores armas contra la oscuridad. "
            "Un cierre épico para una saga que marcó a una generación."
        )
    },
    {
        "id": 47,
        "titulo": "El señor de los anillos: La comunidad del anillo",
        "estreno": 2001,
        "director": "Peter Jackson",
        "generos": ["Fantasía", "Aventura", "Épico"],
        "poster": "",
        "sinopsis": (
            "Frodo Bolsón recibe el Anillo Único y emprende un viaje junto a un grupo de héroes para destruirlo en Mordor. "
            "El camino está lleno de peligros, traiciones y descubrimientos. "
            "El inicio de una trilogía que redefinió el género fantástico. "
            "Un relato épico sobre amistad, poder y esperanza."
        )
    },
    {
        "id": 48,
        "titulo": "El señor de los anillos: El retorno del rey",
        "estreno": 2003,
        "director": "Peter Jackson",
        "generos": ["Fantasía", "Aventura", "Épico"],
        "poster": "",
        "sinopsis": (
            "La guerra por la Tierra Media alcanza su punto culminante. "
            "Mientras Aragorn acepta su destino como rey, Frodo y Sam continúan su peligrosa misión en Mordor. "
            "La lucha entre luz y oscuridad se resuelve en una batalla épica. "
            "Ganadora de 11 premios Óscar, es considerada una de las mayores epopeyas del cine."
        )
    },
    {
        "id": 49,
        "titulo": "Matrix Reloaded",
        "estreno": 2003,
        "director": "Lana Wachowski, Lilly Wachowski",
        "generos": ["Ciencia ficción", "Acción"],
        "poster": "",
        "sinopsis": (
            "Neo, ahora plenamente consciente de sus poderes, lidera la resistencia contra las máquinas. "
            "Junto a Trinity y Morpheus, enfrenta nuevas amenazas y descubre verdades ocultas sobre la Matrix. "
            "Con secuencias de acción espectaculares, expande el universo filosófico de la saga. "
            "Un capítulo intermedio que prepara el clímax final."
        )
    },
    {
        "id": 50,
        "titulo": "Matrix Revolutions",
        "estreno": 2003,
        "director": "Lana Wachowski, Lilly Wachowski",
        "generos": ["Ciencia ficción", "Acción"],
        "poster": "",
        "sinopsis": (
            "La lucha final entre humanos y máquinas se libra tanto en el mundo real como en la Matrix. "
            "Neo enfrenta a Smith en un duelo apocalíptico que definirá el destino de ambos mundos. "
            "La trilogía concluye con un mensaje de sacrificio, esperanza y equilibrio. "
            "Un cierre cargado de simbolismo y épica visual."
        )
    },
        {
        "id": 51,
        "titulo": "Avatar",
        "estreno": 2009,
        "director": "James Cameron",
        "generos": ["Ciencia ficción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Jake Sully, un exmarine en silla de ruedas, es enviado al planeta Pandora para infiltrarse en la cultura Na’vi. "
            "Mientras cumple con su misión militar, se enamora de Neytiri y descubre la profunda conexión de los Na’vi con su mundo. "
            "Debe elegir entre la codicia humana y la preservación de la naturaleza. "
            "Un espectáculo visual que revolucionó el cine en 3D."
        )
    },
    {
        "id": 52,
        "titulo": "Gladiador",
        "estreno": 2000,
        "director": "Ridley Scott",
        "generos": ["Acción", "Drama", "Histórico"],
        "poster": "",
        "sinopsis": (
            "Máximo Décimo Meridio, un general romano traicionado, es condenado a la esclavitud y convertido en gladiador. "
            "Mientras lucha en la arena, busca vengar el asesinato de su familia y la traición de Cómodo, el nuevo emperador. "
            "Una historia de honor, lealtad y justicia en la antigua Roma. "
            "Un clásico moderno que combina épica y emoción."
        )
    },
    {
        "id": 53,
        "titulo": "Coco",
        "estreno": 2017,
        "director": "Lee Unkrich, Adrian Molina",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Miguel, un niño apasionado por la música, se adentra en la Tierra de los Muertos durante el Día de los Muertos. "
            "Allí busca respuestas sobre su familia y descubre secretos enterrados en su árbol genealógico. "
            "Entre canciones y colores, aprende el valor de la memoria y el legado familiar. "
            "Una celebración de la cultura mexicana y de los lazos eternos del amor."
        )
    },
    {
        "id": 54,
        "titulo": "Up",
        "estreno": 2009,
        "director": "Pete Docter",
        "generos": ["Animación", "Aventura", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Carl, un anciano viudo, decide cumplir el sueño de su difunta esposa: viajar a las Cataratas del Paraíso. "
            "Con miles de globos amarrados a su casa, emprende la aventura, sin imaginar que Russell, un niño explorador, lo acompañará. "
            "Enfrentan desafíos y forjan una amistad inesperada. "
            "Un viaje emotivo sobre la pérdida, la esperanza y los nuevos comienzos."
        )
    },
    {
        "id": 55,
        "titulo": "Toy Story",
        "estreno": 1995,
        "director": "John Lasseter",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Woody, un vaquero de juguete, se ve amenazado por la llegada de Buzz Lightyear, un moderno guardián espacial. "
            "La rivalidad entre ambos los lleva a una aventura fuera de la habitación de Andy. "
            "Juntos aprenden sobre la amistad y la lealtad. "
            "La primera película animada por computadora que marcó un antes y un después en el cine."
        )
    },
    {
        "id": 56,
        "titulo": "Toy Story 3",
        "estreno": 2010,
        "director": "Lee Unkrich",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Andy se prepara para ir a la universidad y sus juguetes enfrentan un futuro incierto. "
            "Accidentalmente llegan a una guardería donde no todo es lo que parece. "
            "La historia explora la madurez, el cambio y el adiós. "
            "Un cierre conmovedor que emocionó a toda una generación."
        )
    },
    {
        "id": 57,
        "titulo": "Buscando a Nemo",
        "estreno": 2003,
        "director": "Andrew Stanton",
        "generos": ["Animación", "Aventura", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Marlin, un pez payaso sobreprotector, emprende un viaje a través del océano para rescatar a su hijo Nemo. "
            "En el camino conoce a Dory, una pez con problemas de memoria, que se convierte en su inseparable compañera. "
            "Juntos enfrentan peligros marinos y descubren la importancia de la confianza. "
            "Una aventura entrañable que encantó a niños y adultos por igual."
        )
    },
    {
        "id": 58,
        "titulo": "Los Increíbles",
        "estreno": 2004,
        "director": "Brad Bird",
        "generos": ["Animación", "Acción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "La familia Parr, compuesta por superhéroes obligados a vivir en el anonimato, regresa a la acción cuando surge una nueva amenaza. "
            "Bob, Helen y sus hijos deben unir fuerzas para salvar al mundo. "
            "La película explora la dinámica familiar con humor y acción trepidante. "
            "Un homenaje a los cómics y al valor de la unidad."
        )
    },
    {
        "id": 59,
        "titulo": "Ratatouille",
        "estreno": 2007,
        "director": "Brad Bird",
        "generos": ["Animación", "Comedia", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Remy, una rata con un paladar refinado, sueña con convertirse en chef en París. "
            "Con la ayuda de Linguini, un joven torpe, logra cocinar platos que conquistan a todos. "
            "A pesar de los prejuicios, demuestra que el talento puede surgir en los lugares más inesperados. "
            "Una oda a la pasión culinaria y a la perseverancia."
        )
    },
    {
        "id": 60,
        "titulo": "WALL·E",
        "estreno": 2008,
        "director": "Andrew Stanton",
        "generos": ["Animación", "Ciencia ficción", "Aventura"],
        "poster": "",
        "sinopsis": (
            "WALL·E, un robot compactador de basura, pasa sus días limpiando una Tierra abandonada por los humanos. "
            "Su rutina cambia cuando conoce a EVA, una moderna robot enviada a buscar señales de vida. "
            "Su historia de amor los lleva al espacio en busca de un futuro mejor. "
            "Un relato tierno sobre la soledad, el consumismo y la esperanza."
        )
    },
    {
        "id": 61,
        "titulo": "El viaje de Chihiro",
        "estreno": 2001,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Chihiro, una niña de 10 estrenos, se adentra en un mundo mágico habitado por espíritus y dioses. "
            "Al quedar atrapada, debe trabajar en una casa de bestrenos para recuperar la libertad de sus padres. "
            "En el proceso, aprende sobre valentía y madurez. "
            "Una obra maestra del Studio Ghibli que combina magia y reflexión."
        )
    },
    {
        "id": 62,
        "titulo": "Mi vecino Totoro",
        "estreno": 1988,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Dos hermanas se mudan al campo y descubren a Totoro, una criatura mágica que habita en el bosque cercano. "
            "Juntas viven experiencias maravillosas y fortalecen su unión. "
            "La película transmite la belleza de la infancia y la conexión con la naturaleza. "
            "Un clásico entrañable del cine japonés."
        )
    },
    {
        "id": 63,
        "titulo": "La princesa Mononoke",
        "estreno": 1997,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Ashitaka, un príncipe maldito, viaja en busca de una cura y se encuentra en medio de un conflicto entre humanos e espíritus del bosque. "
            "La princesa Mononoke lucha por proteger la naturaleza de la explotación humana. "
            "La película plantea una reflexión profunda sobre el equilibrio ecológico. "
            "Un relato épico que fusiona acción y espiritualidad."
        )
    },
    {
        "id": 64,
        "titulo": "Akira",
        "estreno": 1988,
        "director": "Katsuhiro Otomo",
        "generos": ["Animación", "Ciencia ficción", "Acción"],
        "poster": "",
        "sinopsis": (
            "En un Tokio postapocalíptico, Kaneda debe rescatar a su amigo Tetsuo, quien desarrolla poderes psíquicos descontrolados. "
            "El gobierno y fuerzas secretas buscan aprovecharse de su poder. "
            "La película revolucionó la animación japonesa con su visión futurista y su compleja narrativa. "
            "Un referente del cyberpunk en la cultura global."
        )
    },
    {
        "id": 65,
        "titulo": "Ghost in the Shell",
        "estreno": 1995,
        "director": "Mamoru Oshii",
        "generos": ["Animación", "Ciencia ficción", "Cyberpunk"],
        "poster": "",
        "sinopsis": (
            "La Mayor Motoko Kusanagi, una cyborg de élite, investiga al misterioso hacker conocido como Puppet Master. "
            "La historia cuestiona la identidad, la conciencia y los límites entre lo humano y lo artificial. "
            "Con un estilo visual impactante, se convirtió en una influencia clave en el cine moderno. "
            "Una obra de culto dentro del anime y la ciencia ficción."
        )
    },
    {
        "id": 66,
        "titulo": "Your Name",
        "estreno": 2016,
        "director": "Makoto Shinkai",
        "generos": ["Animación", "Romance", "Fantasía"],
        "poster": "",
        "sinopsis": (
            "Mitsuha y Taki, dos adolescentes que nunca se han visto, comienzan a intercambiar cuerpos de manera misteriosa. "
            "Mientras intentan adaptarse a las vidas del otro, surge una conexión emocional profunda. "
            "Un destino trágico los obliga a desafiar el tiempo y el espacio. "
            "Un fenómeno global que mezcla romance juvenil y espiritualidad japonesa."
        )
    },
    {
        "id": 67,
        "titulo": "El castillo ambulante",
        "estreno": 2004,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Sophie, una joven convertida en anciana por una maldición, encuentra refugio en el castillo ambulante de Howl, un mago enigmático. "
            "Juntos enfrentan guerras y hechizos mientras descubren el valor del amor. "
            "Con un estilo visual único, la película reflexiona sobre el miedo y la transformación. "
            "Un relato mágico que trasciende la edad y el tiempo."
        )
    },
    {
        "id": 68,
        "titulo": "El niño y la bestia",
        "estreno": 2015,
        "director": "Mamoru Hosoda",
        "generos": ["Animación", "Fantasía", "Aventura"],
        "poster": "",
        "sinopsis": (
            "Ren, un niño huérfano, entra accidentalmente en el reino de las bestias y es adoptado como aprendiz por Kumatetsu, una criatura guerrera. "
            "A lo largo de los estrenos, su relación maestro-discípulo se convierte en un lazo paternal. "
            "La película explora la identidad, el crecimiento personal y la familia elegida. "
            "Un relato vibrante lleno de acción y ternura."
        )
    },
    {
        "id": 69,
        "titulo": "Paprika",
        "estreno": 2006,
        "director": "Satoshi Kon",
        "generos": ["Animación", "Ciencia ficción", "Thriller"],
        "poster": "",
        "sinopsis": (
            "Una psicóloga utiliza un dispositivo que permite entrar en los sueños de los pacientes para tratarlos. "
            "Cuando el aparato es robado, los límites entre realidad y fantasía comienzan a desmoronarse. "
            "La historia combina misterio, surrealismo y exploración psicológica. "
            "Inspiró numerosas obras de ciencia ficción modernas."
        )
    },
    {
        "id": 70,
        "titulo": "Perfect Blue",
        "estreno": 1997,
        "director": "Satoshi Kon",
        "generos": ["Animación", "Thriller", "Psicológico"],
        "poster": "",
        "sinopsis": (
            "Mima, una idol japonesa, decide dejar la música para convertirse en actriz. "
            "A medida que cambia de carrera, comienza a ser acosada por un fan obsesionado y pierde la noción de la realidad. "
            "El filme explora la fama, la obsesión y la identidad con un tono perturbador. "
            "Un thriller psicológico considerado de culto."
        )
    },
    {
        "id": 71,
        "titulo": "Recuerdos del ayer",
        "estreno": 1991,
        "director": "Isao Takahata",
        "generos": ["Animación", "Drama"],
        "poster": "",
        "sinopsis": (
            "Taeko, una mujer de 27 estrenos, viaja al campo y comienza a recordar su infancia. "
            "El contraste entre su vida adulta y los recuerdos de niña la llevan a cuestionar sus decisiones. "
            "Una obra intimista sobre la nostalgia y el paso del tiempo. "
            "Un retrato delicado de la vida cotidiana japonesa."
        )
    },
    {
        "id": 72,
        "titulo": "El cuento de la princesa Kaguya",
        "estreno": 2013,
        "director": "Isao Takahata",
        "generos": ["Animación", "Fantasía", "Drama"],
        "poster": "",
        "sinopsis": (
            "Un humilde campesino encuentra a una diminuta princesa dentro de un bambú. "
            "La niña crece rápidamente y es criada como noble, pero estrenora la libertad de su vida en el campo. "
            "La historia, basada en un antiguo cuento japonés, combina belleza visual y melancolía. "
            "Una obra poética sobre la fugacidad de la vida."
        )
    },
    {
        "id": 73,
        "titulo": "Los niños lobo",
        "estreno": 2012,
        "director": "Mamoru Hosoda",
        "generos": ["Animación", "Fantasía", "Drama"],
        "poster": "",
        "sinopsis": (
            "Hana se enamora de un hombre lobo y juntos tienen dos hijos. "
            "Tras la repentina muerte de su pareja, debe criarlos sola en un entorno rural. "
            "La película explora la maternidad, la identidad y la dualidad entre lo humano y lo animal. "
            "Un relato emotivo que mezcla realismo y fantasía."
        )
    },
    {
        "id": 74,
        "titulo": "El viento se levanta",
        "estreno": 2013,
        "director": "Hayao Miyazaki",
        "generos": ["Animación", "Drama", "Histórico"],
        "poster": "",
        "sinopsis": (
            "Jirō Horikoshi sueña con diseñar aviones y se convierte en ingeniero durante la Segunda Guerra Mundial. "
            "Mientras desarrolla su carrera, vive una historia de amor marcada por la enfermedad. "
            "La película reflexiona sobre los sueños, el progreso y las tragedias de la guerra. "
            "Un adiós poético de Miyazaki antes de su retiro temporal."
        )
    },
    {
        "id": 75,
        "titulo": "Mary and Max",
        "estreno": 2009,
        "director": "Adam Elliot",
        "generos": ["Animación", "Drama"],
        "poster": "",
        "sinopsis": (
            "Mary, una niña australiana solitaria, entabla amistad por carta con Max, un hombre mayor con síndrome de Asperger en Nueva York. "
            "A lo largo de los estrenos, su relación epistolar se convierte en un refugio frente a la soledad. "
            "La animación stop-motion refuerza el tono íntimo y melancólico. "
            "Una conmovedora historia sobre amistad, diferencias y aceptación."
        )
    },
    {
        "id": 76,
        "titulo": "Coraline",
        "estreno": 2009,
        "director": "Henry Selick",
        "generos": ["Animación", "Fantasía", "Terror"],
        "poster": "",
        "sinopsis": (
            "Coraline descubre una puerta secreta en su nueva casa que la conduce a un mundo paralelo. "
            "Aunque al principio parece mejor que su realidad, pronto descubre oscuros secretos. "
            "La película mezcla atmósfera gótica con la inocencia infantil. "
            "Una obra inquietante sobre el deseo y la aceptación."
        )
    },
    {
        "id": 77,
        "titulo": "Klaus",
        "estreno": 2019,
        "director": "Sergio Pablos",
        "generos": ["Animación", "Comedia", "Navidad"],
        "poster": "",
        "sinopsis": (
            "Jesper, un cartero egoísta, es enviado a un pueblo remoto y hostil. "
            "Allí conoce a Klaus, un carpintero que fabrica juguetes, y juntos cambian el destino del lugar. "
            "La película ofrece un nuevo origen para la leyenda de Santa Claus. "
            "Un relato emotivo sobre la bondad y la reconciliación."
        )
    },
    {
        "id": 81,
        "titulo": "Spider-Man: Un nuevo universo",
        "estreno": 2018,
        "director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        "generos": ["Animación", "Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Miles Morales, un adolescente de Brooklyn, se convierte en Spider-Man tras la mordida de una araña radiactiva. "
            "Cuando un colisionador abre portales a otros universos, conoce a diferentes versiones del héroe. "
            "Juntos deberán detener a Kingpin y salvar sus mundos. "
            "Una película innovadora en estilo visual y narrativa que redefinió el cine de superhéroes animados."
        )
    },
    {
        "id": 82,
        "titulo": "El hombre araña",
        "estreno": 2002,
        "director": "Sam Raimi",
        "generos": ["Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Peter Parker, un joven tímido, adquiere poderes tras ser mordido por una araña genética. "
            "Mientras enfrenta al Duende Verde, aprende que 'un gran poder conlleva una gran responsabilidad'. "
            "Un clásico del cine de superhéroes que marcó el inicio de la era moderna del género."
        )
    },
    {
        "id": 83,
        "titulo": "El caballero de la noche asciende",
        "estreno": 2012,
        "director": "Christopher Nolan",
        "generos": ["Acción", "Superhéroes", "Drama"],
        "poster": "",
        "sinopsis": (
            "Ocho estrenos después de asumir la culpa por la muerte de Harvey Dent, Batman vive en el retiro. "
            "La aparición de Bane, un enemigo brutal, lo obliga a regresar y enfrentar la destrucción de Gotham. "
            "La trilogía de Nolan cierra con una reflexión sobre sacrificio y redención."
        )
    },
    {
        "id": 84,
        "titulo": "Logan",
        "estreno": 2017,
        "director": "James Mangold",
        "generos": ["Acción", "Drama", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "En un futuro cercano, un envejecido Logan cuida de un enfermo Profesor X mientras lidia con la decadencia de sus poderes. "
            "Cuando aparece Laura, una niña con habilidades similares, deberá protegerla de fuerzas oscuras. "
            "Un cierre crudo y emotivo para la historia de Wolverine."
        )
    },
    {
        "id": 85,
        "titulo": "Deadpool",
        "estreno": 2016,
        "director": "Tim Miller",
        "generos": ["Acción", "Comedia", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Wade Wilson, un exmercenario, obtiene habilidades regenerativas tras un experimento, pero queda desfigurado. "
            "Adopta la identidad de Deadpool, un antihéroe sarcástico y violento, en busca de venganza. "
            "Rompiendo la cuarta pared, ofrece una visión irreverente del género."
        )
    },
    {
        "id": 86,
        "titulo": "Capitán América: El soldado del invierno",
        "estreno": 2014,
        "director": "Anthony y Joe Russo",
        "generos": ["Acción", "Superhéroes", "Thriller"],
        "poster": "",
        "sinopsis": (
            "Steve Rogers, ahora trabajando para S.H.I.E.L.D., descubre una conspiración que amenaza la libertad mundial. "
            "Enfrenta a un asesino conocido como el Soldado del Invierno, quien resulta ser alguien de su pasado. "
            "Un thriller político disfrazado de película de superhéroes."
        )
    },
    {
        "id": 87,
        "titulo": "Iron Man",
        "estreno": 2008,
        "director": "Jon Favreau",
        "generos": ["Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Tony Stark, un millonario e inventor, construye una armadura de alta tecnología para escapar del cautiverio. "
            "Transformado en Iron Man, se convierte en un héroe que redefine el género. "
            "La película que inició el Universo Cinematográfico de Marvel."
        )
    },
    {
        "id": 88,
        "titulo": "Guardianes de la galaxia",
        "estreno": 2014,
        "director": "James Gunn",
        "generos": ["Acción", "Aventura", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Un grupo de inadaptados galácticos —Peter Quill, Gamora, Drax, Rocket y Groot— se unen para salvar la galaxia de Ronan. "
            "Con humor, música retro y acción, redefinió el concepto de 'equipo de héroes'."
        )
    },
    {
        "id": 89,
        "titulo": "Doctor Strange",
        "estreno": 2016,
        "director": "Scott Derrickson",
        "generos": ["Acción", "Superhéroes", "Fantasía"],
        "poster": "",
        "sinopsis": (
            "Stephen Strange, un neurocirujano arrogante, busca curarse tras un accidente que arruina sus manos. "
            "Encuentra el camino de la magia y se convierte en el Hechicero Supremo. "
            "Visualmente deslumbrante, introduce el misticismo al MCU."
        )
    },
    {
        "id": 90,
        "titulo": "Black Panther",
        "estreno": 2018,
        "director": "Ryan Coogler",
        "generos": ["Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "T’Challa regresa a Wakanda para asumir el trono tras la muerte de su padre. "
            "Enfrenta a Killmonger, un enemigo que desafía su visión del mundo. "
            "Una obra culturalmente influyente que celebró la representación afrodescendiente en el cine."
        )
    },
    {
        "id": 91,
        "titulo": "Thor: Ragnarok",
        "estreno": 2017,
        "director": "Taika Waititi",
        "generos": ["Acción", "Superhéroes", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Thor debe evitar el fin de Asgard mientras enfrenta a su hermana Hela, diosa de la muerte. "
            "Con la ayuda de Hulk y Valkyrie, vive una aventura cósmica llena de humor y colores psicodélicos. "
            "Un giro fresco y cómico dentro del MCU."
        )
    },
    {
        "id": 92,
        "titulo": "Ant-Man",
        "estreno": 2015,
        "director": "Peyton Reed",
        "generos": ["Acción", "Superhéroes", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Scott Lang, un ladrón reformado, se convierte en el sucesor de Hank Pym al portar un traje que lo encoge. "
            "Mientras aprende a ser héroe, enfrenta a un villano con la misma tecnología. "
            "Un relato ligero y entretenido con un enfoque familiar."
        )
    },
    {
        "id": 93,
        "titulo": "Capitana Marvel",
        "estreno": 2019,
        "director": "Anna Boden, Ryan Fleck",
        "generos": ["Acción", "Superhéroes", "Ciencia ficción"],
        "poster": "",
        "sinopsis": (
            "Carol Danvers, una piloto con poderes cósmicos, se convierte en una de las heroínas más poderosas del universo. "
            "Enfrenta a los Skrulls y descubre la verdad sobre su pasado. "
            "Una película clave en la construcción del MCU."
        )
    },
    {
        "id": 94,
        "titulo": "Venom",
        "estreno": 2018,
        "director": "Ruben Fleischer",
        "generos": ["Acción", "Superhéroes", "Ciencia ficción"],
        "poster": "",
        "sinopsis": (
            "Eddie Brock, un periodista, se fusiona con un simbionte alienígena que le otorga poderes extraordinarios. "
            "Aunque su relación es conflictiva, juntos enfrentan amenazas mayores. "
            "Una visión oscura y diferente del universo Marvel."
        )
    },
    {
        "id": 95,
        "titulo": "Shazam!",
        "estreno": 2019,
        "director": "David F. Sandberg",
        "generos": ["Acción", "Superhéroes", "Comedia"],
        "poster": "",
        "sinopsis": (
            "Billy Batson, un adolescente, recibe poderes mágicos que lo transforman en un superhéroe adulto. "
            "Mientras aprende a manejarlos, debe enfrentarse al villano Sivana. "
            "Una mezcla fresca de humor y corazón dentro del DCEU."
        )
    },
    {
        "id": 96,
        "titulo": "Wonder Woman",
        "estreno": 2017,
        "director": "Patty Jenkins",
        "generos": ["Acción", "Superhéroes", "Histórico"],
        "poster": "",
        "sinopsis": (
            "Diana, princesa amazona, deja su isla para detener la Primera Guerra Mundial. "
            "Descubre su verdadero poder y su destino como Wonder Woman. "
            "Un hito para la representación femenina en el cine de superhéroes."
        )
    },
    {
        "id": 97,
        "titulo": "Aquaman",
        "estreno": 2018,
        "director": "James Wan",
        "generos": ["Acción", "Superhéroes", "Fantasía"],
        "poster": "",
        "sinopsis": (
            "Arthur Curry, mitad humano y mitad atlante, debe reclamar su lugar como rey de Atlantis. "
            "Con una estética vibrante y épica submarina, se convierte en un héroe completo. "
            "Una aventura visualmente deslumbrante."
        )
    },
    {
        "id": 98,
        "titulo": "Liga de la Justicia",
        "estreno": 2017,
        "director": "Zack Snyder (versión extendida 2021)",
        "generos": ["Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Tras la muerte de Superman, Batman y Wonder Woman reclutan a nuevos héroes para enfrentar la amenaza de Steppenwolf. "
            "La unión de Flash, Aquaman y Cyborg da forma a la Liga de la Justicia. "
            "Una historia coral que consolidó al DCEU."
        )
    },
    {
        "id": 99,
        "titulo": "El Hombre de Acero",
        "estreno": 2013,
        "director": "Zack Snyder",
        "generos": ["Acción", "Superhéroes"],
        "poster": "",
        "sinopsis": (
            "Clark Kent, un joven con poderes extraordinarios, busca su lugar en el mundo. "
            "Cuando Zod llega a la Tierra, debe asumir su identidad como Superman y salvar a la humanidad. "
            "Un reinicio épico y visualmente imponente."
        )
    },
    {
        "id": 100,
        "titulo": "Batman vs Superman: El amanecer de la justicia",
        "estreno": 2016,
        "director": "Zack Snyder",
        "generos": ["Acción", "Superhéroes", "Drama"],
        "poster": "",
        "sinopsis": (
            "Batman considera a Superman una amenaza para la humanidad, lo que desencadena un enfrentamiento monumental. "
            "Mientras tanto, Lex Luthor manipula los hilos y crea un enemigo aún más peligroso. "
            "Un filme que marcó un punto clave en la construcción del DCEU."
        )
    }

]
#Listado de 50 usuarios (id, usuario, email, img, cantidad_reseñas)
listaUsuarios = [
    {
        "id": 1,
        "usuario": "user1",
        "email": "user1@example.com",
        "img": "",
        "cantidad_reseñas": 5
    },
    {
        "id": 2,
        "usuario": "user2",
        "email": "user2@example.com",
        "img": "",
        "cantidad_reseñas": 3
    },
    {
        "id": 3,
        "usuario": "user3",
        "email": "user3@example.com",
        "img": "",
        "cantidad_reseñas": 7
    },
    {
        "id": 4,
        "usuario": "user4",
        "email": "user4@example.com",
        "img": "",
        "cantidad_reseñas": 2
    },
    {
        "id": 5,
        "usuario": "user5",
        "email": "user5@example.com",
        "img": "",
        "cantidad_reseñas": 10
    },
    {
        "id": 6,
        "usuario": "user6",
        "email": "user6@example.com",
        "img": "",
        "cantidad_reseñas": 1
    },
    {
        "id": 7,
        "usuario": "user7",
        "email": "user7@example.com",
        "img": "",
        "cantidad_reseñas": 4
    },
    {
        "id": 8,
        "usuario": "user8",
        "email": "user8@example.com",
        "img": "",
        "cantidad_reseñas": 6
    },
    {
        "id": 9,
        "usuario": "user9",
        "email": "user9@example.com",
        "img": "",
        "cantidad_reseñas": 9
    },
    {
        "id": 10,
        "usuario": "user10",
        "email": "user10@example.com",
        "img": "",
        "cantidad_reseñas": 8
    },
    {
        "id": 11,
        "usuario": "user11",
        "email": "user11@example.com",
        "img": "",
        "cantidad_reseñas": 0
    },
    {
        "id": 12,
        "usuario": "user12",
        "email": "user12@example.com",
        "img": "",
        "cantidad_reseñas": 12
    },
    {
        "id": 13,
        "usuario": "user13",
        "email": "user13@example.com",
        "img": "",
        "cantidad_reseñas": 15
    },
    {
        "id": 14,
        "usuario": "user14",
        "email": "user14@example.com",
        "img": "",
        "cantidad_reseñas": 2
    },
    {
        "id": 15,
        "usuario": "user15",
        "email": "user15@example.com",
        "img": "",
        "cantidad_reseñas": 5
    },
    {
        "id": 16,
        "usuario": "user16",
        "email": "user16@example.com",
        "img": "",
        "cantidad_reseñas": 7
    },
    {
        "id": 17,
        "usuario": "user17",
        "email": "user17@example.com",
        "img": "",
        "cantidad_reseñas": 11
    },
    {
        "id": 18,
        "usuario": "user18",
        "email": "user18@example.com",
        "img": "",
        "cantidad_reseñas": 6
    },
    {
        "id": 19,
        "usuario": "user19",
        "email": "user19@example.com",
        "img": "",
        "cantidad_reseñas": 13
    },
    {
        "id": 20,
        "usuario": "user20",
        "email": "user20@example.com",
        "img": "",
        "cantidad_reseñas": 9
    },
    {
        "id": 21,
        "usuario": "user21",
        "email": "user21@example.com",
        "img": "",
        "cantidad_reseñas": 1
    },
    {
        "id": 22,
        "usuario": "user22",
        "email": "user22@example.com",
        "img": "",
        "cantidad_reseñas": 3
    },
    {
        "id": 23,
        "usuario": "user23",
        "email": "user23@example.com",
        "img": "",
        "cantidad_reseñas": 14
    },
    {
        "id": 24,
        "usuario": "user24",
        "email": "user24@example.com",
        "img": "",
        "cantidad_reseñas": 7
    },
    {
        "id": 25,
        "usuario": "user25",
        "email": "user25@example.com",
        "img": "",
        "cantidad_reseñas": 4
    },
    {
        "id": 26,
        "usuario": "user26",
        "email": "user26@example.com",
        "img": "",
        "cantidad_reseñas": 8
    },
    {
        "id": 27,
        "usuario": "user27",
        "email": "user27@example.com",
        "img": "",
        "cantidad_reseñas": 6
    },
    {
        "id": 28,
        "usuario": "user28",
        "email": "user28@example.com",
        "img": "",
        "cantidad_reseñas": 10
    },
    {
        "id": 29,
        "usuario": "user29",
        "email": "user29@example.com",
        "img": "",
        "cantidad_reseñas": 12
    },
    {
        "id": 30,
        "usuario": "user30",
        "email": "user30@example.com",
        "img": "",
        "cantidad_reseñas": 2
    },
    {
        "id": 31,
        "usuario": "user31",
        "email": "user31@example.com",
        "img": "",
        "cantidad_reseñas": 9
    },
    {
        "id": 32,
        "usuario": "user32",
        "email": "user32@example.com",
        "img": "",
        "cantidad_reseñas": 7
    },
    {
        "id": 33,
        "usuario": "user33",
        "email": "user33@example.com",
        "img": "",
        "cantidad_reseñas": 11
    },
    {
        "id": 34,
        "usuario": "user34",
        "email": "user34@example.com",
        "img": "",
        "cantidad_reseñas": 0
    },
    {
        "id": 35,
        "usuario": "user35",
        "email": "user35@example.com",
        "img": "",
        "cantidad_reseñas": 4
    },
    {
        "id": 36,
        "usuario": "user36",
        "email": "user36@example.com",
        "img": "",
        "cantidad_reseñas": 13
    },
    {
        "id": 37,
        "usuario": "user37",
        "email": "user37@example.com",
        "img": "",
        "cantidad_reseñas": 15
    },
    {
        "id": 38,
        "usuario": "user38",
        "email": "user38@example.com",
        "img": "",
        "cantidad_reseñas": 1
    },
    {
        "id": 39,
        "usuario": "user39",
        "email": "user39@example.com",
        "img": "",
        "cantidad_reseñas": 5
    },
    {
        "id": 40,
        "usuario": "user40",
        "email": "user40@example.com",
        "img": "",
        "cantidad_reseñas": 14
    },
    {
        "id": 41,
        "usuario": "user41",
        "email": "user41@example.com",
        "img": "",
        "cantidad_reseñas": 3
    },
    {
        "id": 42,
        "usuario": "user42",
        "email": "user42@example.com",
        "img": "",
        "cantidad_reseñas": 9
    },
    {
        "id": 43,
        "usuario": "user43",
        "email": "user43@example.com",
        "img": "",
        "cantidad_reseñas": 6
    },
    {
        "id": 44,
        "usuario": "user44",
        "email": "user44@example.com",
        "img": "",
        "cantidad_reseñas": 2
    },
    {
        "id": 45,
        "usuario": "user45",
        "email": "user45@example.com",
        "img": "",
        "cantidad_reseñas": 12
    },
    {
        "id": 46,
        "usuario": "user46",
        "email": "user46@example.com",
        "img": "",
        "cantidad_reseñas": 7
    },
    {
        "id": 47,
        "usuario": "user47",
        "email": "user47@example.com",
        "img": "",
        "cantidad_reseñas": 8
    },
    {
        "id": 48,
        "usuario": "user48",
        "email": "user48@example.com",
        "img": "",
        "cantidad_reseñas": 10
    },
    {
        "id": 49,
        "usuario": "user49",
        "email": "user49@example.com",
        "img": "",
        "cantidad_reseñas": 5
    },
    {
        "id": 50,
        "usuario": "user50",
        "email": "user50@example.com",
        "img": "",
        "cantidad_reseñas": 11
    },
]


"""
Gestión de Películas (CRUD)
    -Crear, editar, eliminar y mostrar películas.
    -Campos: id, título, estreno, director, géneros, sinopsis.
    -Listado paginado básico.

Gestión de Usuarios (CRUD)
    -Campos: id, usuario, email, cantidad de reseñas.
    -Registro de usuarios.

Reseñas (creación y vinculación básica)
    -Usuario puede asociar reseña a una película.
    -Campos: usuario, película, puntuación, título, comentario.
"""

# ---> Funciones para la gestión de películas (CRUD) <---
def crearPelicula(titulo, estreno, director, generos, poster="", sinopsis=""):

    nuevo_id = max([p["id"] for p in listaPeliculas], default=0) + 1 # En esta linea genero un id unico que siempre va a ser el ultimo mas uno

    nueva_pelicula = {
        "id": nuevo_id,
        "titulo": titulo,
        "estreno": estreno,
        "director": director,
        "generos": generos,
        "poster": poster,
        "sinopsis": sinopsis
    }

    listaPeliculas.append(nueva_pelicula)
    return nueva_pelicula

def editarPelicula():
    return


def eliminarPelicula():
    print("")
    print("----- Eliminar películas -----")
    pelicula_a_eliminar = input('Ingrese el título de la película que desea eliminar o "0" para salir: ')

    while pelicula_a_eliminar != "0":
        peliculaEncontrada = False
        for pelicula in listaPeliculas:
            if pelicula["titulo"].lower() == pelicula_a_eliminar.lower():
                peliculaEncontrada = True
                confirmacion = input(f"¿Está seguro de que desea eliminar '{pelicula['titulo']}'? (Responda: Si / No)")
                while confirmacion.lower() != "si" and confirmacion.lower() != "no":
                    confirmacion = input("Respuesta inválida. Por favor, responda 'Si' o 'No': ")
                if confirmacion.lower() == 'si':
                    listaPeliculas.remove(pelicula)
                    print(f"La película '{pelicula['titulo']}' ha sido eliminada.")
                    print("")
                    pelicula_a_eliminar = input('Ingrese el título de la película que desea eliminar o "0" para salir: ')
                else:
                    print("Eliminación cancelada.")
            else:
                peliculaEncontrada = False
        if peliculaEncontrada == False and pelicula_a_eliminar != "0":
            print("")
            print(f"La película '{pelicula_a_eliminar}' no fue encontrada.")
            pelicula_a_eliminar = input('Ingrese el título de la película que desea eliminar o "0" para salir:')
                    
        


def mostrarPeliculas():
    print("")
    print("----- Listado de películas -----")
    for pelicula in listaPeliculas:
        id = pelicula["id"]
        titulo = pelicula["titulo"]
        estreno = pelicula["estreno"]
        director = pelicula["director"]
        generos = ", ".join(pelicula["generos"])
        sinopsis = pelicula["sinopsis"]
        poster = pelicula["poster"]
        
        print(f"ID: {id} \nTitulo: {titulo} \nEstreno: {estreno} \nTitulo: {titulo} \nDirector: {director} \nGeneros: {generos} \nSinopsis: {sinopsis} \nPoster: {poster}   " )
        print("")
        print("-------------------------------")
        print("")


def crudPeliculas():
    print("----- CRUD de Películas -----")
    print("1. Crear película \n2. Editar película \n3. Eliminar película \n4. Mostrar películas \n5. Volver al menú principal")
    opcionElegida = int(input("Seleccione la opción a ejecutar:"))

    while opcionElegida != 5:
        if opcionElegida == 1:
            crearPelicula()
        elif opcionElegida == 2:
            editarPelicula()
        elif opcionElegida == 3:
            eliminarPelicula()
        elif opcionElegida == 4:
            mostrarPeliculas()
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
        print("1. Crear película \n2. Editar película \n3. Eliminar película \n4. Mostrar películas \n5. Volver al menú principal")
        opcionElegida = int(input("Seleccione la opción a ejecutar: "))
    return

# Gestión de Usuarios (CRUD)
def crearUsuario():
    
    return

def editarUsuario():
    
    return

def eliminarUsuario():
    
    return

def mostrarUsuarios():
    
    return

def crudUsuarios():
    print("----- CRUD de Usuarios -----")
    print("1. Crear usuario \n2. Editar usuario \n3. Eliminar usuario \n4. Mostrar usuarios \n5. Volver al menu principal")
    opcion = int(input("Seleccione la opcion: "))
    while opcion != 5:
        if opcion == 1:
            crearUsuario()
        elif opcion == 2:
            editarUsuario()
        elif opcion == 3:
            eliminarUsuario()
        elif opcion == 4:
            mostrarUsuarios()
        else:
            print("Opción inválida")
        print("\n1. Crear usuario \n2. Editar usuario \n3. Eliminar usuario \n4. Mostrar usuarios \n5. Volver al menu principal")
        opcion = int(input("Seleccione la opcion: "))
    return


# Gestion de Reseñas
def crearReseña():
    
    return

def mostrarReseñas():
    
    return

def crudReseñas():
    print("----- Gestion de Reseñas -----")
    print("1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menu principal")
    opcion = int(input("Seleccione la opcion: "))
    while opcion != 3:
        if opcion == 1:
            crearReseña()
        elif opcion == 2:
            mostrarReseñas()
        else:
            print("Opcion invalida")
        print("\n1. Crear reseña \n2. Mostrar reseñas \n3. Volver al menu principal")
        opcion = int(input("Seleccione la opcion: "))
    return


# Menu Principal
def menuPrincipal():
    print("----- Sistema de Gestion -----")
    print("1. Peliculas \n2. Usuarios \n3. Reseñas \n4. Salir")
    opcion = int(input("Seleccione la opcion: "))
    while opcion != 4:
        if opcion == 1:
            crudPeliculas()
        elif opcion == 2:
            crudUsuarios()
        elif opcion == 3:
            crudReseñas()
        else:
            print("Opcion invalida")
        print("\n1. Peliculas \n2. Usuarios \n3. Reseñas \n4. Salir")
        opcion = int(input("Seleccione la opcion: "))


# Ejecutar menu principal
menuPrincipal()