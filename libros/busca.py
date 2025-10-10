from .alta import pedir_titulo, pedir_autor, pedir_genero, pedir_anio_dc  # Reutiliza la logica de validacion
from .lista import listar_libros                                          # Reutiliza la logica de impresion

# Tabla de estrategias
CRITERIOS = {
    "1": {
        "pedir": pedir_titulo,
        "comparador": lambda libro, q: normalizar(q) in normalizar(libro.get("titulo", "")),
    },
    "2": {
        "pedir": pedir_autor,
        "comparador": lambda libro, q: normalizar(libro.get("autor", "")) == normalizar(q),
    },
    "3": {
        "pedir": pedir_genero,
        "comparador": lambda libro, q: normalizar(libro.get("genero", "")) == normalizar(q),
    },
    "4": {
        "pedir": pedir_anio_dc,
        "comparador": lambda libro, q: libro.get("año") == q,
    },
}


#    ¡¡¡ FUNCION OK !!!
def normalizar(valor):
    return valor.strip().lower()


#    ¡¡¡ FUNCION OK !!!
def buscar_libro(biblioteca):
    # Busca libros en base a un criterio e imprime el resultado

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    print("\nBuscar por:")
    print("1. Título (contiene)")
    print("2. Autor  (exacto)")
    print("3. Género (exacto)")
    print("4. Año    (exacto)")

    # Elige criterio
    while True:
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion in { "1", "2", "3", "4" }:
            break
        print("Opción inválida. Ingrese 1, 2, 3 o 4.")

    # Obtiene valor del usuario
    valor = CRITERIOS[opcion]["pedir"]()

    # Filtra usando el comparador
    equivale = CRITERIOS[opcion]["comparador"]
    resultados = [libro for libro in biblioteca if equivale(libro, valor)]

    if not resultados:
        print("\nNo se encontraron libros para ese criterio.")
        return

    # Reusa el mismo formato de impresión
    listar_libros(resultados)
