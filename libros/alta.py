import re
from datetime import datetime


# Patrones para REGEX
RX_TITULO   = re.compile(r"^[A-Za-z0-9ÁÉÍÓÚÜÑáéíóúüñ ,.'-]+$")   # Títulos: mayusculas, minusculas, números, acentos, dieresis, eñes, espacios, etc.
RX_AUTOR    = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ .,'-]+$")      # Autor: mayusculas, minusculas, acentos, dieresis, eñes, espacios, etc.
RX_GENERO   = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$")          # Género: mayusculas, minusculas, acentos, dieresis, eñes, espacios, etc.
RX_ANIO     = re.compile(r"^\d{1,4}$")                           # 1-4 dígitos (Solo Libros D.C).


def ingresar(msj, normalizar, validar, transformar, error_msj="Valor inválido."):
    # Bucle generico de entrada, normaliza, valida y transforma en caso de ser necesario
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
    

# Funciones específicas
def pedir_titulo():
    print("\n")
    return ingresar(
        "🔍 Título Del Libro: ",
        normalizar=True,
        validar=lambda s: bool(RX_TITULO.match(s)),
        transformar=False,
        error_msj="Título inválido: use letras, números, espacios y . , ' -",
    )


def pedir_autor():
    return ingresar(
        "✍️  Autor Del Libro: ",
        normalizar=True,
        validar=lambda s: bool(RX_AUTOR.match(s)),
        transformar=False,
        error_msj="Autor inválido: use solo letras, espacios y . , ' -",
    )


def pedir_genero():
    return ingresar(
        "🧩 Género Literario: ",
        normalizar=True,
        validar=lambda s: bool(RX_GENERO.match(s)),
        transformar=False,
        error_msj="Género inválido: use solo letras y espacios.",
    )


def pedir_anio_dc():
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
    # Valida duplicados, devuelve un Booleano

    tittle = titulo.lower()
    author = autor.lower()
    return any(libro["Título"].strip().lower() == tittle and libro["Autor"].strip().lower() == author for libro in biblioteca)


def alta_libro(biblioteca):
    # Orquestador para la carga de libros

    Título = pedir_titulo()
    Autor  = pedir_autor()
    genero = pedir_genero()
    anio   = pedir_anio_dc()

    if existe_duplicado(biblioteca, Título, Autor):
        print("Este libro ya está registrado (mismo título y autor).")
        return

    nuevo = {
        "Título": Título,
        "Autor": Autor,
        "Género": genero,
        "Año": anio,
        "Estado": "Disponible",
    }
    biblioteca.append(nuevo)
    print ("\n")
    print("Libro agregado ✅")
    print ("\n")
