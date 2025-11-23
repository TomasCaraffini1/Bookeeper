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
