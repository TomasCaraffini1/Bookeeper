from datetime import datetime

def registrar_prestamo(historial, dni, titulo):
    fecha = str(datetime.now()).split('.')[0]  # Fecha y hora sin microsegundos
    historial.append({
        "DNI": dni,
        "Libro": titulo,
        "Fecha": fecha,
        "Estado": "Activo"
    })

def registrar_devolucion(historial, dni, titulo):
    for h in historial:
        if h["DNI"] == dni and h["Libro"] == titulo and h["Estado"] == "Activo":
            h["Estado"] = "Devuelto"
            h["Fecha_devolucion"] = str(datetime.now()).split('.')[0]
            return
    print("⚠️ No se encontró un préstamo activo para ese socio y libro.")

def mostrar_historial(historial):
    if not historial:
        print("\nNo hay registros de préstamos.\n")
        return
    print("\n=== Historial de préstamos ===")
    for h in historial:
        estado = h["Estado"]
        print(f"- {h['Libro']} | DNI {h['DNI']} | {estado} | {h['Fecha']}")
    print()

def mostrar_historial_por_socio(historial, socios):
    print("\n=== Historial por socio ===")

    if not historial:
        print("No hay movimientos registrados.")
        return

    if not socios:
        print("No hay socios cargados.")
        return

    dni = input("Ingrese el DNI del socio: ").strip()

    # validar que exista
    socio = next((s for s in socios if s['DNI'] == dni), None)

    if not socio:
        print("❌ No existe un socio con ese DNI.")
        return

    print(f"\n📚 Movimientos del socio: {socio['Nombre']} (DNI: {dni})\n")

    movimientos = [m for m in historial if m['DNI'] == dni]

    if not movimientos:
        print("Este socio no tiene movimientos registrados.")
        return

    for m in movimientos:
        print(f"- {m['Fecha']} | {m['Estado']} | {m['Libro']}")

    print()


def mostrar_historial_libros(historial, libros):
    print("\n=== Historial por libro ===")

    if not historial:
        print("No hay movimientos registrados.")
        return

    titulo = input("Ingrese el título del libro: ").strip()

    # validar que exista
    libro = next((l for l in libros if l['Título'].lower() == titulo.lower()), None)

    if not libro:
        print("❌ No existe un libro con ese título.")
        return

    print(f"\n📖 Movimientos del libro: {libro['Título']}\n")
    print(f"Veces alquilado: {libro.get('veces_alquilado', 0)}\n")

    movimientos = [m for m in historial if m['Libro'].lower() == titulo.lower()]

    if not movimientos:
        print("Este libro no tiene movimientos registrados.")
        return

    for m in movimientos:
        print(f"- {m.get('Fecha', '---')} | {m.get('Estado', '---')} | DNI: {m.get('DNI', '---')}")


    print()
