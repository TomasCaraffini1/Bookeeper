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
        if len(fila["titulo"]) > titulo_width:
            titulo_width = len(fila["titulo"])
        if len(fila["autor"]) > autor_width:
            autor_width = len(fila["autor"])
        if len(fila["genero"]) > genero_width:
            genero_width = len(fila["genero"])
        if len(str(fila["año"])) > anio_width:
            anio_width = len(str(fila["año"]))
        if len(fila["estado"]) > estado_width:
            estado_width = len(fila["estado"])

    

    # Encabezado
    print()
    print( encabezado[0].ljust(titulo_width) + " " + encabezado[1].ljust(autor_width) + " " + encabezado[2].ljust(genero_width) + " " + encabezado[3].ljust(anio_width) + " " +
        encabezado[4].ljust(estado_width) )
    
    # Filas
    for fila in biblioteca:
        print(
            fila["titulo"].ljust(titulo_width) + " " +
            fila["autor"].ljust(autor_width) + " " +
            fila["genero"].ljust(genero_width) + " " +
            str(fila["año"]).ljust(anio_width) + " " +
            fila["estado"].ljust(estado_width)
        )
    print()


