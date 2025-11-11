import json
import os
from libros.alta import alta_libro
from libros.lista import listar_libros
from libros.busca import buscar_libro
from libros.alquiler import prestar_libro, devolver_libro
from libros.socios import registrar_socio, listar_socios
from libros.historial import mostrar_historial

def cargar_datos(archivo="datos.json"):
    """
    Carga los datos desde un archivo JSON.
    Si el archivo no existe, está vacío o tiene una estructura incorrecta,
    devuelve un diccionario con listas vacías.
    """
    if not os.path.exists(archivo):
        print(f"⚠️ Advertencia: No se encontró '{archivo}'. Se creará uno nuevo al salir.")
        return {"libros": [], "socios": [], "historial": []}

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

            # Si el contenido es una lista (versión vieja del archivo)
            if type(datos) is list:
                print("⚠️ El archivo contenía una lista antigua. Se migrará a la nueva estructura.")
                return {"libros": datos, "socios": [], "historial": []}

            # Si faltan claves, las completa
            if "libros" not in datos or "socios" not in datos or "historial" not in datos:
                print(f"⚠️ Estructura de datos incompleta. Se inicializan listas vacías.")
                nuevos_datos = {"libros": [], "socios": [], "historial": []}
                if "libros" in datos:
                    nuevos_datos["libros"] = datos["libros"]
                if "socios" in datos:
                    nuevos_datos["socios"] = datos["socios"]
                if "historial" in datos:
                    nuevos_datos["historial"] = datos["historial"]
                return nuevos_datos

            return datos

    except json.JSONDecodeError:
        print(f"⚠️ Advertencia: El archivo '{archivo}' está vacío o malformado. Iniciando con datos vacíos.")
        return {"libros": [], "socios": [], "historial": []}



def guardar_datos(libros, archivo="datos.json"):
    """
    Guarda la lista de libros (que está en Python) en el archivo JSON.
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
    print("========================================")
    print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("========================================")
    print("1. Alta de libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Préstamo de libro")
    print("5. Devolución de libro")
    print("6. Registrar socio")
    print("7. Listar socios")
    print("8. Ver historial de préstamos")
    print("9. Salir")
    print("========================================")


# lee y valida la opcion del usuario, retorna opcion valida entre 1 y 6
def elegir_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-9): "))
            if 1 <= opcion <= 9:
                return opcion
            else:
                print("❌ Error: Ingrese un número entre 1 y 9.")
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero.")

def main():
    datos = cargar_datos("datos.json")
    libros = datos.get("libros", [])
    socios = datos.get("socios", [])
    historial = datos.get("historial", [])

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
            prestar_libro(libros, socios, historial)
        elif opcion == 5:
            devolver_libro(libros, socios, historial)
        elif opcion == 6:
            registrar_socio(socios)
        elif opcion == 7:
            listar_socios(socios)
        elif opcion == 8:
            mostrar_historial(historial)
        elif opcion == 9:
            guardar_datos({"libros": libros, "socios": socios, "historial": historial}, "datos.json")
            print("\nGracias por utilizar Bookeeper!👋\n")
            break


####################################### Programa Principal ##############################

if __name__ == "__main__":
    main()
