import os
from utils.corefiles import leer_json

RUTA_EQUIPOS = os.path.join("data", "equipos.json")
RUTA_JUGADORES = os.path.join("data", "jugadores.json")
RUTA_TRANSFERENCIAS = os.path.join("data", "transferencias.json")

def ver_estadisticas():
    equipos = leer_json(RUTA_EQUIPOS)
    jugadores = leer_json(RUTA_JUGADORES)
    transferencias = leer_json(RUTA_TRANSFERENCIAS)

    print("\n📊 Estadísticas Generales\n")
    print(f"Total equipos registrados: {len(equipos)}")

    jugadores_por_equipo = {}
    for jugador in jugadores.values():
        eq_id = jugador["equipo_id"]
        jugadores_por_equipo[eq_id] = jugadores_por_equipo.get(eq_id, 0) + 1

    print("Jugadores por equipo:")
    for eq_id, count in jugadores_por_equipo.items():
        print(f"- Equipo ID {eq_id}: {count} jugador(es)")

    print(f"Total transferencias registradas: {len(transferencias)}")
