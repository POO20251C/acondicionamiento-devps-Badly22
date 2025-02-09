def invertir_lista():
    numeros = input("Ingrese una lista de números separados por espacios: ").strip()
    lista_invertida = " ".join(reversed(numeros.split()))
    print(lista_invertida)

invertir_lista()
