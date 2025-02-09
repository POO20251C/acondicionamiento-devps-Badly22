def contar_palabras():
    cadena = input("Ingrese una cadena de texto: ").strip()
    cantidad = len(cadena.split())
    print(cantidad)

contar_palabras()