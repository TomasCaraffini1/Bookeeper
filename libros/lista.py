def listar_libros(biblioteca):
    """
    Muestra en pantalla una tabla con todos los libros.
    Si la lista está vacía, informa que no hay libros para mostrar.

    Argumentos:
        biblioteca (list[dict]): Lista de libros almacenados.

    """

    if not biblioteca:
        print("\nNo hay libros para mostrar. ❌\n")
        return

    encabezado = ["Título", "Autor", "Género", "Año", "Estado"]

    # Anchos dinámicos
    titulo_w = max(len(encabezado[0]), *(len(f["titulo"]) for f in biblioteca))
    autor_w  = max(len(encabezado[1]), *(len(f["autor"])  for f in biblioteca))
    genero_w = max(len(encabezado[2]), *(len(f["genero"]) for f in biblioteca))
    anio_w = 4
    estado_w = 10

    # Calcula largo total de la tabla e imprime con una funcion lambda
    largo = 21 + titulo_w + autor_w + genero_w + anio_w + estado_w
    separador = lambda x: print("-" * x)

    print()
    # Encabezado
    separador(largo)
    print(f"| {encabezado[0].ljust(titulo_w)}  | {encabezado[1].ljust(autor_w)}  | {encabezado[2].ljust(genero_w)}  | {encabezado[3].ljust(anio_w)}  | {encabezado[4].ljust(estado_w)}  |")

    # Filas
    separador(largo)
    for f in biblioteca:
        print(f"| {f["titulo"].ljust(titulo_w)}  | {f["autor"].ljust(autor_w)}  | {f["genero"].ljust(genero_w)}  | {str(f["anio"]).ljust(anio_w)}  | {f["estado"].ljust(estado_w)}  |")
    separador(largo)


def formatear_libros(biblioteca):
    """
    Devuelve una lista de TUPLAS (titulo, autor, estado)
    utilizando map() para transformar la estructura original.

    Argumentos:
        biblioteca (list[dict]): Lista de libros almacenados.
    
    Devuelve:
        list[tuple]: lista de TUPLAS utilizando map().

    """

    return list(map(
        lambda libro: (libro["titulo"], libro["autor"], libro["estado"]),
        biblioteca
    ))


def mostrar_resumen_libros(biblioteca):
    """
    Muestra en pantalla una tabla con 3 columnas (Título, Autor, Estado).
    
    Argumentos:
        biblioteca (list[dict]): Lista de libros almacenados.

    """

    filas = formatear_libros(biblioteca)

    if not filas:
        print("\nNo hay libros cargados.\n")
        return

    encabezados = ["Título", "Autor", "Estado"]

    # Cálculo del ancho de cada columna
    col_widths = [
        max(len(encabezados[i]), max(len(f[i]) for f in filas))
        for i in range(3)
    ]

    # Línea separadora
    separador = "-" * (sum(col_widths) + 10)

    print()
    print(separador)

    # Encabezados
    print(
        f"| {encabezados[0].ljust(col_widths[0])} "
        f"| {encabezados[1].ljust(col_widths[1])} "
        f"| {encabezados[2].ljust(col_widths[2])} |"
    )
    print(separador)

    # Filas
    for titulo, autor, estado in filas:
        print(
            f"| {titulo.ljust(col_widths[0])} "
            f"| {autor.ljust(col_widths[1])} "
            f"| {estado.ljust(col_widths[2])} |"
        )

    print(separador)
    print()
