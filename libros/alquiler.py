from .lista import listar_libros     # Reutiliza la lógica de impresión
from .busca import pedir_y_filtrar   # Reutiliza la lógica de búsqueda


def listar_coincidencias(resultados):
    """
    Muestra una tabla con los libros que coincidieron con la búsqueda.

    La tabla incluye un índice numérico para permitir la selección posterior
    por parte del usuario.

    Argumentos:
        resultados (list[dict]): Lista de libros que cumplen con el criterio de búsqueda.

    """

    if not resultados:
        print("\nNo hay coincidencias. ❌")
        print()
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

    # Filas con índice, manteniendo el mismo espaciado y ljust
    for i, f in enumerate(resultados, start=1):
        print(
            f"| {str(i).ljust(indice_w)}  | "
            f"{f['titulo'].ljust(titulo_w)}  | "
            f"{f['autor'].ljust(autor_w)}  | "
            f"{f['genero'].ljust(genero_w)}  | "
            f"{str(f['anio']).ljust(anio_w)}  | "
            f"{f['estado'].ljust(estado_w)}  |"
        )

    separador(largo)


def elegir_de_lista(resultados):
    """
    Permite al usuario seleccionar un libro de una lista de coincidencias.

    Si solo existe una coincidencia, se selecciona automáticamente.
    Si el usuario ingresa 0, se cancela la operación y se retorna None.

    Argumentos:
        resultados (list[dict]): Lista de libros coincidentes.

    Devuelve:
        int | None: Índice (0-based) del libro seleccionado, o None si se cancela.
        
    """

    print("\nCoincidencias encontradas:")
    print("--------------------------")
    listar_coincidencias(resultados)

    if not resultados:
        return None

    if len(resultados) == 1:
        print("\nSe encontró 1 coincidencia, seleccionada automáticamente 🎯.")
        return 0

# Valida la seleccion y devuelve el indice de la misma
    while True:
        print()
        seleccion = input(f"Elija 1-{len(resultados)} (o 0 para cancelar): ").strip()

        if seleccion == '0':
            print("Operación cancelada.")
            return None

        if seleccion.isdigit():
            indice = int(seleccion)
            if 1 <= indice <= len(resultados):
                return indice - 1  

        print(f"Selección inválida. Ingrese un número entre 1 y {len(resultados)}.")


def prestar_libro(biblioteca):
    """
    Realiza el préstamo de un libro, cambiando su estado a "Alquilado".

    El usuario primero realiza una búsqueda, luego selecciona un libro
    y, si está disponible, se actualiza su estado.

    Argumentos:
        biblioteca (list[dict]): Lista completa de libros cargados.

    """

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    resultados = pedir_y_filtrar(biblioteca)

    # Vuelve al menú si el usuario presionó '0' en el sub-menú de búsqueda
    if resultados is None:
        return

    indice = elegir_de_lista(resultados)

    # Si el índice es None (porque no hubo resultados o se canceló),
    # detenemos la función aquí y volvemos al menú.
    if indice is None:
        return

    libro = resultados[indice]

    # Valida que este Disponible
    estado_actual = libro.get("estado", "")
    if estado_actual.lower() != "disponible".lower():
        print(f"\nNo se puede prestar. El libro está: {estado_actual}")
        print("Solo se pueden prestar libros disponibles.")
        return

    libro["estado"] = "Alquilado"
    print("\n✅ Préstamo registrado. Libro actualizado:")
    listar_libros([libro])
    print()


def devolver_libro(biblioteca):
    """
    Registra la devolución de un libro, cambiando su estado a "Disponible".

    Argumentos:
        biblioteca (list[dict]): Lista completa de libros cargados.

    """

    if not biblioteca:
        print("\nNo hay libros cargados.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    
    # Vuelve al menú si el usuario presionó '0' en el sub-menú de búsqueda
    if resultados is None:
        return

    indice = elegir_de_lista(resultados)

    # Aplicamos la misma validación que en prestar_libro
    if indice is None:
        return

    libro = resultados[indice]

    # Valida que este Alquilado
    estado_actual = libro.get("estado", "")
    if estado_actual.lower() != "alquilado".lower():
        print(f"\nNo se puede devolver. El libro está: {estado_actual}")
        print("Solo se pueden devolver libros alquilados.")
        return

    libro["estado"] = "Disponible"
    print("\n✅ Devolución registrada. Libro actualizado:")
    listar_libros([libro])
