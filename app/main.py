import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import controllers.equipos as equipos
import controllers.jugadores as jugadores
import controllers.transferencias as transferencias
import controllers.estadisticas as estadisticas

def menu():
    while True:
        print("\n=== GESTOR DE TORNEOS INTERNACIONALES ===")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Transferencia de jugador (venta o préstamo)")
        print("6. Ver estadísticas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            equipos.registrar_equipo()
        elif opcion == "2":
            equipos.listar_equipos()
        elif opcion == "3":
            jugadores.registrar_jugador()
        elif opcion == "4":
            jugadores.listar_jugadores()
        elif opcion == "5":
            transferencias.realizar_transferencia()
            transferencias.listar_transferencias()
        elif opcion == "6":
            estadisticas.ver_estadisticas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
