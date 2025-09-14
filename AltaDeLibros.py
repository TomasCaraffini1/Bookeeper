# Función para dar de alta un libro
def alta_libro(biblioteca):
    titulo = input("Título Del Libro: ")
    autor = input("Autor: ")
    genero = input("Género Literario: ")
    año = input("Año: ")

    if titulo == "" or autor == "" or genero == "" or año == "":
        print("Complete por favor todos los campos.")
        return

    try:
        año = int(año)
    except ValueError:
        print("El año debe ser un número.")
        return

    nuevo = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año,
        "estado": "disponible"
    }

    biblioteca.append(nuevo)
    print("Libro agregado.")
