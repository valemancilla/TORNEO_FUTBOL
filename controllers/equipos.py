import os
import json
from utils.corefiles import leer_json, guardar_json
from utils.validatedata import input_obligatorio



RUTA_EQUIPOS = os.path.join("data", "equipos.json")

def registrar_equipo():
    print("\n=== Registro de Nuevo Equipo ===")
    
    nombre = input_obligatorio("📌 Nombre del equipo: ")
    fundacion = input_obligatorio("📅 Fecha de fundación (ej: 1947-03-07): ")
    pais = input_obligatorio("🌍 País: ")
    liga_id = input_obligatorio("🏷 ID de la liga: ")

    # Leer archivo de equipos
    equipos = leer_json(RUTA_EQUIPOS)

    
    nuevo_equipo = {
        "id": len(equipos) + 1,
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais,
        "liga_id": liga_id
    }

    # Agregar y guardar
    equipos.append(nuevo_equipo)
    guardar_json(RUTA_EQUIPOS, equipos)
    print("✅ Equipo registrado correctamente.")

def listar_equipos():
    equipos = leer_json(RUTA_EQUIPOS)
    
    if not equipos:
        print("\n📭 No hay equipos registrados.")
        return

    print("\n📋 Lista de Equipos Registrados:\n")
    print("{:<5} {:<25} {:<15} {:<15} {:<10}".format("ID", "Nombre", "Fundación", "País", "Liga"))
    print("-" * 75)
    
    for eq in equipos:
        print("{:<5} {:<25} {:<15} {:<15} {:<10}".format(
            eq["id"], eq["nombre"], eq["fundacion"], eq["pais"], eq["liga_id"]
        ))

