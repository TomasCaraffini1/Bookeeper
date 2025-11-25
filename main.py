import json
import os
from libros.alta import alta_libro
from libros.lista import listar_libros,mostrar_resumen_libros
from libros.busca import buscar_libro, mostrar_disponibles
from libros.alquiler import prestar_libro, devolver_libro
from libros.socios import registrar_socio, listar_socios
from libros.historial import mostrar_historial
from libros.historial import mostrar_historial_por_socio
from libros.historial import mostrar_historial_libros

def limpiar_consola():
    """
    Limpia la consola realizando un salto grande de líneas.

    Nota:
        Debido a que el programa funciona en múltiples entornos
        (Sistemas Operartivos / IDEs), esta técnica evita depender de
        comandos específicos del sistema operativo.

    """
    
    print("\n" * 100)

def pausar():
    """
    Pausa la ejecución hasta que el usuario presione ENTER.

    Después de confirmar, limpia la consola para mantener
    una interfaz ordenada entre cada operación.

    """
    
    input("\n👉 Presione ENTER para continuar... ✨")
    limpiar_consola()

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
    print("📚 BOOKEEPER")
    print("========================================")
    print("1. Alta de libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Préstamo de libro")
    print("5. Devolución de libro")
    print("6. Ver libros disponibles")
    print("7. Ver resumen de libros")
    print("8. Registrar socio")
    print("9. Listar socios")
    print("10. Ver historial de préstamos (general)")
    print("11. Ver historial por socio")
    print("12. Ver historial por libro")
    print("0. Salir")
    print("========================================")


# lee y valida la opcion del usuario, retorna opcion valida entre 1 y 6
def elegir_opcion():
    """
    Solicita y valida que el usuario elija una opción del menú principal.

    Acepta únicamente números enteros entre 1 y 8.

    Devuelve:
        int: Opción seleccionada.

    """
    while True:
        try:
            opcion = int(input("Seleccione una opción (0-12): "))
            if 0 <= opcion <= 12:
                return opcion
            else:
                print("❌ Error: Ingrese un número entre 0 y 12.")
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
    datos = cargar_datos("datos.json")
    libros = datos.get("libros", [])
    socios = datos.get("socios", [])
    historial = datos.get("historial", [])

    # Asegurar campo de contador en libros
    for libro in libros:
        if "veces_alquilado" not in libro:
            libro["veces_alquilado"] = 0
        

    # Asegurar historial por socio
    for socio in socios:
        if "historial" not in socio:
            socio["historial"] = []
    
    print(f"\nSistema iniciado. Se cargaron {len(libros)} libros desde datos.json.\n")

    while True:
        mostrar_menu()
        opcion = elegir_opcion()

        if opcion == 1:
            alta_libro(libros)
            pausar()
        elif opcion == 2:
            listar_libros(libros)
            pausar()
        elif opcion == 3:
            buscar_libro(libros)
            pausar()
        elif opcion == 4:
            prestar_libro(libros, socios, historial)
            pausar()
        elif opcion == 5:
            devolver_libro(libros, socios, historial)
            pausar()
        elif opcion == 6:
            mostrar_disponibles(libros)
            pausar()
        elif opcion == 7:
            mostrar_resumen_libros(libros)
            pausar()
        elif opcion == 8:
            registrar_socio(socios)
            pausar()
        elif opcion == 9:
            listar_socios(socios)
            pausar()
        elif opcion == 10:
            mostrar_historial(historial)
            pausar()
        elif opcion == 11:
            mostrar_historial_por_socio(historial, socios)
            pausar()
        elif opcion == 12:
            mostrar_historial_libros(historial, libros)
            pausar()
        elif opcion == 0:
            guardar_datos({"libros": libros, "socios": socios, "historial": historial}, "datos.json")
            print("\nGracias por utilizar Bookeeper!👋\n")
            break


####################################### Programa Principal ##############################

if __name__ == "__main__":
    main()
