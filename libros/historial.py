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
