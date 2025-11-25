from .lista import listar_libros     # Reutiliza la logica de impresion
from .busca import pedir_y_filtrar   # Reutiliza la logica de busqueda
from .historial import registrar_prestamo, registrar_devolucion

def listar_coincidencias(resultados):
    """
    Muestra una tabla con los libros que coincidieron con la búsqueda.

    La tabla incluye un índice numérico para permitir la selección posterior
    por parte del usuario.

    Argumentos:
        resultados (list[dict]): Lista de libros que cumplen con el criterio de búsqueda.

    """

    if not resultados:
        print("\nNo hay coincidencias. ❌")
        print("\n")
        return

    # Encabezados (agregamos la columna de índice "#")
    encabezado = ["#", "Título", "Autor", "Género", "Año", "Estado"]

    # Anchos dinámicos (mismo criterio que listar_libros) + índice
    indice_w = len(str(len(resultados)))
    titulo_w = max(len(encabezado[1]), *(len(f["Título"]) for f in resultados))
    autor_w  = max(len(encabezado[2]), *(len(f["Autor"])  for f in resultados))
    genero_w = max(len(encabezado[3]), *(len(f["Género"]) for f in resultados))
    anio_w   = 4
    estado_w = 10

    # Calcula largo total de la tabla e imprime con una funcion lambda
    largo = 25 + indice_w + titulo_w + autor_w + genero_w + anio_w + estado_w
    separador = lambda x: print("-" * x)

    print()
    # Encabezado
    separador(largo)
    print(f"| {encabezado[0].ljust(indice_w)}  | {encabezado[1].ljust(titulo_w)}  | {encabezado[2].ljust(autor_w)}  | {encabezado[3].ljust(genero_w)}  | {encabezado[4].ljust(anio_w)}  | {encabezado[5].ljust(estado_w)}  |")
    separador(largo)

    # Filas con índice (1-based), manteniendo el mismo espaciado y ljust
    for i, f in enumerate(resultados, start=1):
        print(
            f"| {str(i).ljust(indice_w)}  | "
            f"{f['Título'].ljust(titulo_w)}  | "
            f"{f['Autor'].ljust(autor_w)}  | "
            f"{f['Género'].ljust(genero_w)}  | "
            f"{str(f['Año']).ljust(anio_w)}  | "
            f"{f['Estado'].ljust(estado_w)}  |"
        )

    separador(largo)


def elegir_de_lista(resultados):
    """
    Permite al usuario seleccionar un libro de una lista de coincidencias.

    Si solo existe una coincidencia, se selecciona automáticamente.
    Si el usuario ingresa 0, se cancela la operación y se retorna None.

    Argumentos:
        resultados (list[dict]): Lista de libros coincidentes.

    Devuelve:
        int | None: Índice (0-based) del libro seleccionado, o None si se cancela. 
    """
    print("\nCoincidencias encontradas:")
    print("--------------------------")
    listar_coincidencias(resultados)
 
# Si la lista de resultados está vacía, no hay nada que elegir.
# Devolvemos None para que la función que llamó (prestar/devolver) sepa que no se seleccionó nada.
    if not resultados:
        return None

    if len(resultados) == 1:
        print("\n")
        print("Se encontró 1 coincidencia, seleccionada automáticamente 🎯.")
        return 0

# Valida la seleccion y devuelve el indice de la misma
    while True:
# Agregamos la opción "0 para cancelar" para evitar bucles
        print("\n")
        seleccion = input(f"Elija 1-{len(resultados)} (o 0 para cancelar): ").strip()

        if seleccion == '0':
            print("Operación cancelada.")
            return None # Devolvemos None también si el usuario cancela

        if seleccion.isdigit():
            indice = int(seleccion)
            if 1 <= indice <= len(resultados):
                return indice - 1 # Devolvemos el índice (basado en 0)
        print(f"Selección inválida. Ingrese un número entre 1 y {len(resultados)}.")


# Funciones específicas
def prestar_libro(biblioteca, socios, historial):
    """
    Realiza el préstamo de un libro, cambiando su estado a "Alquilado".

    El usuario primero realiza una búsqueda, luego selecciona un libro
    y, si está disponible, se actualiza su estado.

    Argumentos:
        biblioteca (list[dict]): Lista completa de libros cargados.

    """
    if not biblioteca:
        print("\nNo hay libros cargados.")
        return
    if not socios:
        print("\nNo hay socios registrados. Registre uno antes de prestar.")
        return

    dni = input("Ingrese el DNI del socio: ").strip()
    socio = next((s for s in socios if s["DNI"] == dni), None)
    if not socio:
        print("❌ Socio no encontrado.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    indice = elegir_de_lista(resultados)
    if indice is None:
        return

    libro = resultados[indice]
    if libro["Estado"].lower() != "disponible":
        print(f"❌ El libro está {libro['Estado']}.")
        return

    # Cambiar estado del libro
    libro["Estado"] = "Alquilado"

    # Sumar contador al libro
    if "veces_alquilado" not in libro:
        libro["veces_alquilado"] = 0
    libro["veces_alquilado"] += 1

    # Registrar historial EN EL SOCIO
    if "historial" not in socio:
        socio["historial"] = []
    socio["historial"].append({
        "Libro": libro["Título"],
        "Estado": "Activo"
    })

    # Mantener historial global (si querés)
    registrar_prestamo(historial, dni, libro["Título"])


def devolver_libro(biblioteca, socios, historial):
    """
    Registra la devolución de un libro, cambiando su estado a "Disponible".

    Argumentos:
        biblioteca (list[dict]): Lista completa de libros cargados.

    """
    if not biblioteca:
        print("\nNo hay libros cargados.")
        return
    if not socios:
        print("\nNo hay socios registrados.")
        return
        
    dni = input("Ingrese el DNI del socio: ").strip()
    socio = next((s for s in socios if s["DNI"] == dni), None)
    if not socio:
        print("❌ Socio no encontrado.")
        return

    resultados = pedir_y_filtrar(biblioteca)
    indice = elegir_de_lista(resultados)
    if indice is None:
        return

    libro = resultados[indice]
    
    if libro["Estado"].lower() != "alquilado":
        print(f"❌ El libro está {libro['Estado']}.")
        return

    libro["Estado"] = "Disponible"
    if "historial" not in socio:
        socio["historial"] = []
    socio["historial"].append({
        "Libro": libro["Título"],
        "Estado": "Devuelto"
    })

    registrar_devolucion(historial, dni, libro["Título"])


