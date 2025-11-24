import re
from datetime import datetime


# Patrones para REGEX
RX_TITULO = re.compile(r"^[A-Za-z0-9ÁÉÍÓÚÜÑáéíóúüñ ,.'-]+$")   # Títulos: mayusculas, minusculas, números, acentos, dieresis, eñes, espacios, etc.
RX_AUTOR  = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ .,'-]+$")      # Autor: mayusculas, minusculas, acentos, dieresis, eñes, espacios, etc.
RX_GENERO = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$")          # Género: mayusculas, minusculas, acentos, dieresis, eñes, espacios, etc.
RX_ANIO   = re.compile(r"^\d{1,4}$")                           # 1-4 dígitos (Solo Libros D.C).


def ingresar(msj, normalizar, validar, transformar, error_msj="Valor inválido."):
    """
    Captura y valida entrada del usuario de manera genérica.

    Aplica normalización, validación y transformación según los parámetros
    enviados. Es la base común para las funciones de ingreso de datos.

    Argumentos:
        msj (str): Mensaje mostrado al usuario.
        normalizar (bool): Indica si debe aplicarse strip() al texto ingresado.
        validar (callable | None): Función que valida el valor ingresado.
        transformar (callable | None): Convierte el valor antes de retornarlo.
        error_msj (str): Mensaje mostrado si la validación falla.

    Devuelve:
        Valor ingresado, validado y transformado.
    """

    while True:
        valor = input(msj)

        # Valida si necesito normalizar
        valor = valor.strip() if normalizar else valor

        # Valida que haya un input
        if not valor:
            print("El campo no puede estar vacío.")
            continue
        
        # Valida el input
        if validar and not validar(valor):
            print(error_msj)
            continue

        # Valida y devuelve el tipo del input
        return transformar(valor) if transformar else valor


def pedir_titulo():
    """
    Solicita el título del libro y valida su formato.

    Devuelve:
        str: Título ingresado.
    """

    print()
    return ingresar(
        "🔍 Título Del Libro: ",
        normalizar=True,
        validar=lambda s: bool(RX_TITULO.match(s)),
        transformar=False,
        error_msj="Título inválido: use letras, números, espacios y . , ' -",
    )


def pedir_autor():
    """
    Solicita el autor del libro y valida su formato.

    Devuelve:
        str: Autor ingresado.
    """

    return ingresar(
        "✍️  Autor Del Libro: ",
        normalizar=True,
        validar=lambda s: bool(RX_AUTOR.match(s)),
        transformar=False,
        error_msj="Autor inválido: use solo letras, espacios y . , ' -",
    )


def pedir_genero():
    """
    Solicita el género literario del libro.

    Devuelve:
        str: Género ingresado.
    """

    return ingresar(
        "🧩 Género Literario: ",
        normalizar=True,
        validar=lambda s: bool(RX_GENERO.match(s)),
        transformar=False,
        error_msj="Género inválido: use solo letras y espacios.",
    )


def pedir_anio_dc():
    """
    Solicita el año de publicación (solo Años D.C.).
    Valida que el valor ingresado sea un número entre 1 y el año actual.

    Devuelve:
        int: Año de publicación.
    """
    
    anio_actual = datetime.now().year

    def _validar(s: str) -> bool:
        if not RX_ANIO.match(s):
            return False
        n = int(s)
        return 1 <= n <= anio_actual

    return ingresar(
        "📅 Año - D.C.: ",
        normalizar=True,
        validar=_validar,
        transformar=int,
        error_msj=f"Año inválido: entre 1 y {datetime.now().year}."
    )


def existe_duplicado(biblioteca, titulo, autor):
    """
    Verifica si ya existe un libro registrado con mismo título y autor.

    Argumentos:
        biblioteca (list[dict]): Lista de libros existentes.
        titulo (str): Título del libro.
        autor (str): Autor del libro.

    Devuelve:
        bool: True si ya existe un duplicado, False en caso contrario.
    """

    tittle = titulo.lower()
    author = autor.lower()
    return any(libro["titulo"].strip().lower() == tittle and libro["autor"].strip().lower() == author for libro in biblioteca)


def alta_libro(biblioteca):
    """
    Registra un nuevo libro en la biblioteca.

    Se solicita:
        - Título
        - Autor
        - Género
        - Año

    Valida duplicados antes de agregarlo.

    Argumentos:
        biblioteca (list[dict]): Lista de libros cargados.

    """

    titulo = pedir_titulo()
    autor  = pedir_autor()
    genero = pedir_genero()
    anio   = pedir_anio_dc()

    if existe_duplicado(biblioteca, titulo, autor):
        print("Este libro ya está registrado (mismo título y autor).")
        return

    nuevo = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "anio": anio,
        "estado": "Disponible",
    }
    biblioteca.append(nuevo)
    print("\nLibro agregado ✅\n")
