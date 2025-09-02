def listar_libros(biblioteca):
    # Muestra por pantalla la lista de libros

    # Valido que la biblioteca NO este vacia
    if not biblioteca:
        print()
        print("No hay libros cargados.")
        return

   
    encabezado = ["Título", "Autor", "Género", "Año", "Estado"]

    # Calculo el ancho del encabezado
    titulo_width = len(encabezado[0])
    autor_width = len(encabezado[1])
    genero_width = len(encabezado[2])
    anio_width = len(encabezado[3])
    estado_width = len(encabezado[4])

    # Valido el ancho necesario para el listado
    for fila in biblioteca:
        if len(fila[0]) > titulo_width:
            titulo_width = len(fila[0])
        if len(fila[1]) > autor_width:
            autor_width = len(fila[1])
        if len(fila[2]) > genero_width:
            genero_width = len(fila[2])
        if len(str(fila[3])) > anio_width:
            anio_width = len(str(fila[3]))
        if len(fila[4]) > estado_width:
            estado_width = len(fila[4])


    # Encabezado
    print()
    print( encabezado[0].ljust(titulo_width) + " " + encabezado[1].ljust(autor_width) + " " + encabezado[2].ljust(genero_width) + " " + encabezado[3].ljust(anio_width) + " " +
        encabezado[4].ljust(estado_width) )
    
    # Filas
    for fila in biblioteca:
        print( fila[0].ljust(titulo_width) + " " + fila[1].ljust(autor_width) + " " + fila[2].ljust(genero_width) + " " + str(fila[3]).ljust(anio_width) + " " +
            fila[4].ljust(estado_width) )
    print()
