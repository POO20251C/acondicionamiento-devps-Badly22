def contar_vocales(cadena: str) -> int:
  return sum(1 for c in cadena.lower() if c in "aeiou")

cadena = input("Ingrese una cadena de texto: ")
print(contar_vocales(cadena))

