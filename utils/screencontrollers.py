import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar_pantalla():
    input("\nPresiona ENTER para continuar...")
