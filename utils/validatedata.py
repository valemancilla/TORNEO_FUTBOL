def input_obligatorio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("⚠️ Este campo es obligatorio. Intenta de nuevo.")
