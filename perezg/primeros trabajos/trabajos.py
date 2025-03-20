n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))


suma_total = n1 + n2 + n3


maximo = max(n1, n2, n3)
minimo = min(n1, n2, n3)

medio = suma_total - maximo - minimo

print(f"El valor del medio es: {medio}")