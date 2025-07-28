import os
from utils.corefiles import leer_json, guardar_json
from utils.validatedata import input_obligatorio

RUTA = os.path.join("data", "jugadores.json")
RUTA_EQUIPOS = os.path.join("data", "equipos.json")

def registrar_jugador():
    print("\n👤 Registro de Jugador")
    nombre = input_obligatorio("Nombre: ")
    posicion = input_obligatorio("Posición: ")
    numero = input_obligatorio("Número dorsal: ")
    equipo_id = input_obligatorio("ID del equipo: ")

    equipos = leer_json(RUTA_EQUIPOS)
    if equipo_id not in equipos:
        print("⚠️ El equipo no existe. Registra el equipo primero.")
        return

    jugadores = leer_json(RUTA)
    nuevo_id = str(len(jugadores) + 1)

    nuevo = {
        "id": int(nuevo_id),
        "nombre": nombre,
        "posicion": posicion,
        "numero": numero,
        "equipo_id": equipo_id
    }

    jugadores[nuevo_id] = nuevo
    guardar_json(RUTA, jugadores)
    print("✅ Jugador registrado correctamente.")

def listar_jugadores():
    jugadores = leer_json(RUTA)
    equipos = leer_json(RUTA_EQUIPOS)

    if not jugadores:
        print("📭 No hay jugadores registrados.")
        return

    print("\n📋 Lista de Jugadores Registrados:\n")
    print("{:<5} {:<25} {:<15} {:<10} {:<20}".format("ID", "Nombre", "Posición", "Número", "Equipo"))
    print("-" * 80)

    for jg in jugadores.values():
        equipo_nombre = equipos.get(jg["equipo_id"], {}).get("nombre", "Desconocido")
        print("{:<5} {:<25} {:<15} {:<10} {:<20}".format(
            jg["id"], jg["nombre"], jg["posicion"], jg["numero"], equipo_nombre
        ))
