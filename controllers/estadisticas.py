from utils.corefiles import leer_json
import os
import json

def ver_estadisticas():
    equipos = leer_json(os.path.join("data", "equipos.json"))
    jugadores = leer_json(os.path.join("data", "jugadores.json"))
    transferencias = leer_json(os.path.join("data", "transferencias.json"))

    print("\n📊 Estadísticas Generales:")
    print(f"Total de equipos: {len(equipos)}")
    print(f"Total de jugadores: {len(jugadores)}")
    print(f"Total de transferencias registradas: {len(transferencias)}")