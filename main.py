
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("========================================")
    print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("========================================")
    print("1. Alta de libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Préstamo de libro")
    print("5. Devolución de libro")
    print("6. Salir")
    print("========================================")

# lee y valida la opcion del usuario, retorna opcion valida entre 1 y 6
def elegir_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("❌ Error: Ingrese un número entre 1 y 6.")
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero.")

def main():
    # lista global de los libros
    libros = []
    
    while True:
        mostrar_menu()
        opcion = elegir_opcion()

        if opcion == 1:
            alta_libro(libros)
        elif opcion == 2:
            listar_libros(libros)
        elif opcion == 3:
            buscar_libro(libros)
        elif opcion == 4:
            prestar_libro(libros)
        elif opcion == 5:
            devolver_libro(libros)
        elif opcion == 6:
            print("Gracias por utilizar Bookeeper!👋")
            break

####################################### Programa Principal ##############################

if __name__ == "__main__":
    main()