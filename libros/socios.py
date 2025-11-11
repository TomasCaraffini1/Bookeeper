def registrar_socio(socios):
    print("\n=== Registro de nuevo socio ===")
    nombre = input("👤 Nombre completo: ").strip()
    while not nombre or any(c.isdigit() for c in nombre):
        print("❌ Nombre inválido. Solo letras y espacios.")
        nombre = input("👤 Nombre completo: ").strip()

    dni = input("🪪 DNI: ").strip()
    while not dni.isdigit() or len(dni) < 7 or len(dni) > 8 or any(s['DNI'] == dni for s in socios):
        if not dni.isdigit() or len(dni) < 7 or len(dni) > 8:
            print("❌ DNI inválido (7 u 8 dígitos numéricos).")
        else:
            print("⚠️ Ya existe un socio con ese DNI.")
        dni = input("🪪 DNI: ").strip()

    socios.append({"Nombre": nombre, "DNI": dni})
    print(f"\n✅ Socio '{nombre}' registrado con éxito.\n")

def listar_socios(socios):
    if not socios:
        print("\nNo hay socios registrados.\n")
        return
    print("\n=== Lista de socios ===")
    for s in socios:
        print(f"- {s['Nombre']} (DNI: {s['DNI']})")
    print()
