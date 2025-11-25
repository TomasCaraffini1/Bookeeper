from .alta import pedir_titulo, pedir_autor, pedir_genero, pedir_anio_dc  # Reutiliza la logica de validacion
from .lista import listar_libros                                          # Reutiliza la logica de impresion


# Criterios de Busqueda
CRITERIOS = {
    "1": {
        "pedir": pedir_titulo,
        "comparador": lambda libro, q: normalizar(q) in normalizar(libro.get("Título", "")),
    },
    "2": {
        "pedir": pedir_autor,
        "comparador": lambda libro, q: normalizar(q) in normalizar(libro.get("Autor", ""))
    },
    "3": {
        "pedir": pedir_genero,
        "comparador": lambda libro, q: normalizar(libro.get("Género", "")) == normalizar(q),
    },
    "4": {
        "pedir": pedir_anio_dc,
        "comparador": lambda libro, q: libro.get("Año") == q,
    },
}

def obtener_disponibles(biblioteca):
    """
    Obtiene todos los libros con estado "Disponible".

    Argumentos:
        biblioteca (list[dict]): Lista de libros cargados.

    Devuelve:
        list[dict]: Libros cuyo estado es "Disponible".
    
    """

    return list(filter(lambda libro: libro["Estado"].lower() == "disponible", biblioteca))

def normalizar(valor):
    """
    Convierte un string a minúsculas y elimina espacios en los extremos.

    Argumentos:
        valor (str): Texto a normalizar.

    Devuelve:
        str: Texto normalizado.

    """
    return valor.strip().lower()


def pedir_y_filtrar(biblioteca):
    """
    Solicita al usuario un criterio de búsqueda y filtra la biblioteca.

    El usuario puede buscar por:
        1. Título (parcial)
        2. Autor (parcial)
        3. Género (exacto)
        4. Año (exacto)
        0. Volver

    Argumentos:
        biblioteca (list[dict]): Lista de libros.

    Devuelve:
        list[dict] | None: Libros que cumplen la condición, o None si se cancela.
    """

    print("\nBuscar por:")
    print("1. Título (parcial)")
    print("2. Autor  (parcial)")
    print("3. Género (exacto)")
    print("4. Año    (exacto)")
    print("0. Volver al menu principal.")

    # Elige criterio
    while True:
        opcion = input("Seleccione una opción (0-4): ").strip()
        if opcion == "0":
            print("\nVolviendo al menu principal.")
            return None

        if opcion in {"1", "2", "3", "4"}:
            break

        print("Opción inválida. Ingrese 0, 1, 2, 3 o 4.")

    # Obtiene valor del usuario
    valor = CRITERIOS[opcion]["pedir"]()

    # Filtra usando el comparador
    equivale = CRITERIOS[opcion]["comparador"]

    # Devuelve resultados
    return [libro for libro in biblioteca if equivale(libro, valor)]


def buscar_libro(biblioteca):
    """
    Ejecuta el proceso completo de búsqueda de libros.
    Muestra resultados y reintegra el formato estándar de impresión.

    Argumentos:
        biblioteca (list[dict]): Lista de libros cargados.
    """
    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    
    # Vuelve al menú si el usuario presionó '0' en el sub-menú de búsqueda
    if resultados is None:
        return

    if not resultados:
        print("\nNo se encontraron resultados. Intente otra búsqueda.")
        return

    cantidad = len(resultados)
    if cantidad == 1:
        print(f"\nSe encontró {cantidad} resultado 🎯:\n")
    else:
        print(f"\nSe encontraron {cantidad} resultados 🎯:\n")
    
    # Reusa el mismo formato de impresión
    listar_libros(resultados)
    print()

def mostrar_disponibles(biblioteca):
    """
    Muestra en pantalla únicamente los libros cuyo estado es "Disponible".

    Reutiliza la función `listar_libros()` para mantener el mismo
    formato de tabla en la impresión.

    Argumentos:
        biblioteca (list[dict]): Lista de libros almacenados.
    
    """

    disponibles = obtener_disponibles(biblioteca)

    listar_libros(disponibles)