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


def normalizar(valor):
    return valor.strip().lower()


def pedir_y_filtrar(biblioteca):
    # Busca libros en base a un criterio, devuelve una lista con el resultado

    print("\nBuscar por:")
    print("1. Título (parcial)")
    print("2. Autor  (parcial)")
    print("3. Género (exacto)")
    print("4. Año    (exacto)")

    # Elige criterio
    while True:
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion in {"1", "2", "3", "4"}:
            break
        print("Opción inválida. Ingrese 1, 2, 3 o 4.")

    # Obtiene valor del usuario
    valor = CRITERIOS[opcion]["pedir"]()

    # Filtra usando el comparador
    equivale = CRITERIOS[opcion]["comparador"]

    # Devuelve resultados
    return [libro for libro in biblioteca if equivale(libro, valor)]


def buscar_libro(biblioteca):
    # Orquestador para buscar libros

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return 

    resultados = pedir_y_filtrar(biblioteca)

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
    print("\n")
