"""
Autor: valentina mancilla
Fecha: 2025-07-27
Descripción: torneo de futbol 2.0 ligabet play
"""
import json
import os

# Configuración y funciones utilitarias
from ..config import DB_FILE
from utils.validatedata import validateInt, validatetext, validateflot
from utils.screencontrollers import pausar_pantalla, limpiar_pantalla
from utils.corefiles import readJson, writeJson, updateJson, deleteJson, initializeJson

# Controladores de funciones principales
from controllers import equipos, jugadores, transferencias, estadisticas

def menu():
    while True:
        limpiar_pantalla()
        print("=== GESTOR DE TORNEOS INTERNACIONALES ===")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Transferencia de jugador (venta o préstamo)")
        print("6. Ver estadísticas")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            equipos.registrar_equipo()
            pausar_pantalla()
        elif opcion == "2":
            equipos.listar_equipos()
            pausar_pantalla()
        elif opcion == "3":
            jugadores.registrar_jugador()
            pausar_pantalla()
        elif opcion == "4":
            jugadores.listar_jugadores()
            pausar_pantalla()
        elif opcion == "5":
            transferencias.transferir_jugador()
            pausar_pantalla()
        elif opcion == "6":
            estadisticas.ver_estadisticas()
            pausar_pantalla()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")
            pausar_pantalla()

if __name__ == "__main__":
    menu()