import math

def es_primo(n):

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limite = math.isqrt(n) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

try:
    numero = int(input("Ingrese un número entero positivo: "))
    if es_primo(numero):
        print(f" {numero} es un número primo")
    else:
        print(f" {numero} NO es un número primo")
except ValueError:
    print("Error: Debe ingresar un número entero válido")