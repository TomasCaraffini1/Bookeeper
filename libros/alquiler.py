from .lista import listar_libros     # Reutiliza la logica de impresion
from .busca import pedir_y_filtrar   # Reutiliza la logica de busqueda


def listar_coincidencias(resultados):
    # Muestra por pantalla la lista de coincidencias con un índice al inicio

    if not resultados:
        print("\nNo hay coincidencias. ❌")
        print("\n")
        return

    # Encabezados (agregamos la columna de índice "#")
    encabezado = ["#", "Título", "Autor", "Género", "Año", "Estado"]

    # Anchos dinámicos (mismo criterio que listar_libros) + índice
    indice_w = len(str(len(resultados)))
    titulo_w = max(len(encabezado[1]), *(len(f["titulo"]) for f in resultados))
    autor_w  = max(len(encabezado[2]), *(len(f["autor"])  for f in resultados))
    genero_w = max(len(encabezado[3]), *(len(f["genero"]) for f in resultados))
    anio_w   = 4
    estado_w = 10

    # Calcula largo total de la tabla e imprime con una funcion lambda
    largo = 25 + indice_w + titulo_w + autor_w + genero_w + anio_w + estado_w
    separador = lambda x: print("-" * x)

    print()
    # Encabezado
    separador(largo)
    print(f"| {encabezado[0].ljust(indice_w)}  | {encabezado[1].ljust(titulo_w)}  | {encabezado[2].ljust(autor_w)}  | {encabezado[3].ljust(genero_w)}  | {encabezado[4].ljust(anio_w)}  | {encabezado[5].ljust(estado_w)}  |")
    separador(largo)

    # Filas con índice (1-based), manteniendo el mismo espaciado y ljust
    for i, f in enumerate(resultados, start=1):
        print(
            f"| {str(i).ljust(indice_w)}  | "
            f"{f['titulo'].ljust(titulo_w)}  | "
            f"{f['autor'].ljust(autor_w)}  | "
            f"{f['genero'].ljust(genero_w)}  | "
            f"{str(f['año']).ljust(anio_w)}  | "
            f"{f['estado'].ljust(estado_w)}  |"
        )

    separador(largo)


def elegir_de_lista(resultados):
# Muestra las posibles coincidencias
    print("\nCoincidencias encontradas:")
    print("--------------------------")
    listar_coincidencias(resultados)
 
# Si la lista de resultados está vacía, no hay nada que elegir.
# Devolvemos None para que la función que llamó (prestar/devolver) sepa que no se seleccionó nada.
    if not resultados:
        return None

    if len(resultados) == 1:
        print("Se encontró 1 coincidencia, seleccionada automáticamente.")
        return 0

# Valida la seleccion y devuelve el indice de la misma
    while True:
# Agregamos la opción "0 para cancelar" para evitar bucles

        seleccion = input(f"Elija 1-{len(resultados)} (o 0 para cancelar): ").strip()

        if seleccion == '0':
            print("Operación cancelada.")
            return None # Devolvemos None también si el usuario cancela

        if seleccion.isdigit():
            indice = int(seleccion)
            if 1 <= indice <= len(resultados):
                return indice - 1 # Devolvemos el índice (basado en 0)
        print("Selección inválida.")


# Funciones específicas
def prestar_libro(biblioteca):
# Presta un libro y modifica su estado

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    indice = elegir_de_lista(resultados)

# Si el índice es None (porque no hubo resultados o se canceló),
# detenemos la función aquí y volvemos al menú.
    if indice is None:
        return

    libro = resultados[indice]
    # Valida que este Disponible
    if libro.get("estado", "").lower() != "disponible".lower():
        print(f"\nNo se puede prestar. Estado actual: {libro.get('estado', '')}")
        return

    libro["estado"] = "Alquilado"
    print("\n✅ Préstamo registrado. Libro actualizado:")
    listar_libros([libro])


def devolver_libro(biblioteca):
# Devuelve un libro y modifica su estado

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    indice = elegir_de_lista(resultados)

# Aplicamos la misma validación que en prestar_libro
    if indice is None:
        return

    libro = resultados[indice]

# Valida que este Alquilado
    if libro.get("estado", "").lower() != "alquilado".lower():
        print(f"\nNo se puede devolver. Estado actual: {libro.get('estado', '')}")
        return

    libro["estado"] = "Disponible"
    print("\n✅ Devolución registrada. Libro actualizado:")
    listar_libros([libro])
