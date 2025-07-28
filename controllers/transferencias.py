from utils.corefiles import leer_json, guardar_json
import os
from datetime import datetime
import json

RUTA_JUGADORES = os.path.join("data", "jugadores.json")
RUTA_TRANSFERENCIAS = os.path.join("data", "transferencias.json")

def transferir_jugador():
    jugador_id = int(input("ID del jugador: "))
    nuevo_equipo = input("ID del equipo destino: ")
    tipo = input("Tipo de transferencia (venta/préstamo): ").lower()
    fecha = datetime.now().strftime("%Y-%m-%d")

    jugadores = leer_json(RUTA_JUGADORES)
    transferencias = leer_json(RUTA_TRANSFERENCIAS)

    jugador = next((j for j in jugadores if j["id"] == jugador_id), None)

    if jugador:
        transferencia = {
            "jugador_id": jugador_id,
            "origen": jugador["equipo_id"],
            "destino": nuevo_equipo,
            "tipo": tipo,
            "fecha": fecha
        }
        transferencias.append(transferencia)

        if tipo == "venta":
            jugador["equipo_id"] = nuevo_equipo  # Se actualiza el equipo del jugador

        guardar_json(RUTA_TRANSFERENCIAS, transferencias)
        guardar_json(RUTA_JUGADORES, jugadores)
        print("✅ Transferencia realizada.")
    else:
        print("❌ Jugador no encontrado.")