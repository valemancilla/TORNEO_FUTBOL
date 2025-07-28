import os
from utils.corefiles import leer_json, guardar_json
from utils.validatedata import input_obligatorio

RUTA = os.path.join("data", "equipos.json")

def registrar_equipo():
    print("\n📘 Registro de Equipo")
    nombre = input_obligatorio("Nombre: ")
    fundacion = input_obligatorio("Fecha de fundación (AAAA-MM-DD): ")
    pais = input_obligatorio("País: ")
    liga_id = input_obligatorio("ID de liga: ")

    equipos = leer_json(RUTA)

    nuevo_id = str(len(equipos) + 1)

    nuevo = {
        "id": int(nuevo_id),
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais,
        "liga_id": liga_id
    }

    equipos[nuevo_id] = nuevo
    guardar_json(RUTA, equipos)
    print("✅ Equipo registrado correctamente.")

def listar_equipos():
    equipos = leer_json(RUTA)
    if not equipos:
        print("📭 No hay equipos registrados.")
        return

    print("\n📋 Lista de Equipos Registrados:\n")
    print("{:<5} {:<25} {:<15} {:<15} {:<10}".format("ID", "Nombre", "Fundación", "País", "Liga"))
    print("-" * 75)

    for eq in equipos.values():
        print("{:<5} {:<25} {:<15} {:<15} {:<10}".format(
            eq["id"], eq["nombre"], eq["fundacion"], eq["pais"], eq["liga_id"]
        ))
