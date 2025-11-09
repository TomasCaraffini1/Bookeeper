def listar_libros(biblioteca):
    # Muestra por pantalla la lista de libros

    if not biblioteca:
        print("\n")
        print("\nNo hay libros cargados. ❌")
        print("\n")
        return

    encabezado = ["Título", "Autor", "Género", "Año", "Estado"]

    # Anchos dinámicos
    titulo_w = max(len(encabezado[0]), *(len(f["Título"]) for f in biblioteca))
    autor_w  = max(len(encabezado[1]), *(len(f["Autor"])  for f in biblioteca))
    genero_w = max(len(encabezado[2]), *(len(f["Género"]) for f in biblioteca))
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
        print(f"| {f["Título"].ljust(titulo_w)}  | {f["Autor"].ljust(autor_w)}  | {f["Género"].ljust(genero_w)}  | {str(f["Año"]).ljust(anio_w)}  | {f["Estado"].ljust(estado_w)}  |")
    separador(largo)
