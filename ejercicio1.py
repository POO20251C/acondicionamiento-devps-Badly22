def suma_de_digitos(n):
  return sum(int(d) for d in str(abs(n)))

n = int(input("Ingrese un número: "))
print("La suma de los dígitos es:", suma_de_digitos(n))

