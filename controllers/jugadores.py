from utils.corefiles import leer_json, guardar_json
import os
import json

RUTA_JUGADORES = os.path.join("data", "jugadores.json")

def registrar_jugador():
    nombre = input("Nombre del jugador: ")
    posicion = input("Posición: ")
    dorsal = input("Número dorsal: ")
    equipo_id = input("ID del equipo: ")

    jugadores = leer_json(RUTA_JUGADORES)

    nuevo_jugador = {
        "id": len(jugadores) + 1,
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "equipo_id": equipo_id
    }

    jugadores.append(nuevo_jugador)
    guardar_json(RUTA_JUGADORES, jugadores)
    print("✅ Jugador registrado correctamente.")

def listar_jugadores():
    jugadores = leer_json(RUTA_JUGADORES)
    print("\n👥 Lista de Jugadores:")
    for j in jugadores:
        print(f"{j['id']} - {j['nombre']} ({j['posicion']}) - Equipo ID: {j['equipo_id']}")