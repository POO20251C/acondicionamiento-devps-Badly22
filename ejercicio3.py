def es_palindromo(cadena: str) -> str:
  cadena_limpia = "".join(c for c in cadena.lower() if c.isalnum())
  return "Sí" if cadena_limpia == cadena_limpia[::-1] else "No"

cadena = input("Ingrese una cadena de texto: ")
print(es_palindromo(cadena))
