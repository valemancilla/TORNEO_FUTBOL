import os
from utils.corefiles import leer_json, guardar_json
from utils.validatedata import input_obligatorio

RUTA_JUGADORES = os.path.join("data", "jugadores.json")
RUTA_TRANSFERENCIAS = os.path.join("data", "transferencias.json")
RUTA_EQUIPOS = os.path.join("data", "equipos.json")

def realizar_transferencia():
    print("\n🔄 Transferencia de Jugador")
    jugador_id = input_obligatorio("ID del jugador: ")
    equipo_destino = input_obligatorio("ID del equipo destino: ")
    tipo = input_obligatorio("Tipo de transferencia (venta/préstamo): ")
    fecha = input_obligatorio("Fecha (AAAA-MM-DD): ")

    jugadores = leer_json(RUTA_JUGADORES)
    equipos = leer_json(RUTA_EQUIPOS)
    transferencias = leer_json(RUTA_TRANSFERENCIAS)

    if jugador_id not in jugadores:
        print("⚠️ El jugador no existe.")
        return

    if equipo_destino not in equipos:
        print("⚠️ El equipo destino no existe.")
        return

    jugador = jugadores[jugador_id]
    equipo_origen = jugador["equipo_id"]

    # Actualizar el equipo del jugador solo si es venta
    if tipo.lower() == "venta":
        jugador["equipo_id"] = equipo_destino
        jugadores[jugador_id] = jugador
        guardar_json(RUTA_JUGADORES, jugadores)

    nuevo_id = str(len(transferencias) + 1)
    transferencia = {
        "id": int(nuevo_id),
        "id_jugador": jugador_id,
        "origen": equipo_origen,
        "destino": equipo_destino,
        "tipo": tipo.lower(),
        "fecha": fecha
    }
    transferencias[nuevo_id] = transferencia
    guardar_json(RUTA_TRANSFERENCIAS, transferencias)
    print("✅ Transferencia registrada correctamente.")

def listar_transferencias():
    transferencias = leer_json(RUTA_TRANSFERENCIAS)
    jugadores = leer_json(RUTA_JUGADORES)
    equipos = leer_json(RUTA_EQUIPOS)

    if not transferencias:
        print("📭 No hay transferencias registradas.")
        return

    print("\n📋 Historial de Transferencias:\n")
    print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<12}".format(
        "ID", "Jugador", "Equipo Origen", "Equipo Destino", "Tipo", "Fecha"
    ))
    print("-" * 100)

    for tr in transferencias.values():
        jugador_nombre = jugadores.get(tr["id_jugador"], {}).get("nombre", "Desconocido")
        origen_nombre = equipos.get(tr["origen"], {}).get("nombre", "Desconocido")
        destino_nombre = equipos.get(tr["destino"], {}).get("nombre", "Desconocido")
        print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<12}".format(
            tr["id"], jugador_nombre, origen_nombre, destino_nombre, tr["tipo"], tr["fecha"]
        ))
