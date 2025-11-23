import json
import os
from libros.alta import alta_libro
from libros.lista import listar_libros
from libros.busca import buscar_libro
from libros.alquiler import prestar_libro, devolver_libro


def cargar_datos(archivo="datos.json"):
    """
    Carga los libros desde un archivo JSON.
    Si el archivo no existe o está corrupto, devuelve una lista vacía.

    Argumentos:
        archivo (str): Nombre del archivo JSON.

    Devuelve:
        list[dict]: Lista de libros cargados.

    """
    if not os.path.exists(archivo):
        print(f"⚠️ Advertencia: No se encontró '{archivo}'. Se creará uno nuevo al salir.")
        return [] # Retorna una lista vacía si el archivo no existe

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            # json.load() lee el archivo y convierte el JSON a una lista de Python
            datos = json.load(f)
            return datos
        
    except json.JSONDecodeError:
        print(f"⚠️ Advertencia: El archivo '{archivo}' está vacío o malformado. Iniciando con lista vacía.")
        return []


def guardar_datos(libros, archivo="datos.json"):
    """
    Guarda la lista de libros en un archivo JSON.

    Argumentos:
        libros (list[dict]): Lista completa de libros.
        archivo (str): Nombre del archivo destino.

    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            # json.dump() convierte la lista de Python a formato JSON y la escribe
            # indent=4 hace que el archivo JSON sea legible
            json.dump(libros, f, indent=4)
        print(f"✅ Datos guardados exitosamente en '{archivo}'.")
    except Exception as e:
        print(f"❌ Error al guardar los datos en '{archivo}': {e}")


def mostrar_menu():
    """
    Muestra el menú principal del sistema Bookeeper.

    """
    print("========================================")
    print("📚BOOKEEPER")
    print("========================================")
    print("1. Alta de libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Préstamo de libro")
    print("5. Devolución de libro")
    print("6. Salir")
    print("========================================")


def elegir_opcion():
    """
    Solicita y valida que el usuario elija una opción del menú principal.

    Acepta únicamente números enteros entre 1 y 6.

    Devuelve:
        int: Opción seleccionada.

    """
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            print("❌ Error: Ingrese un número entre 1 y 6.")
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero.")


def main():
    """
    Función principal del programa.

    Flujo:
        1. Carga los datos desde el archivo.
        2. Muestra el menú principal.
        3. Ejecuta la acción elegida.
        4. Guarda los datos al salir.
        
    """
    libros = cargar_datos("datos.json")
    print(f"\nSistema iniciado. Se cargaron {len(libros)} libros desde datos.json.\n")

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
            guardar_datos(libros, "datos.json")
            print("\nGracias por utilizar Bookeeper!👋\n")
            break

####################################### Programa Principal ##############################

if __name__ == "__main__":
    main()
