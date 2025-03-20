import random

numero_secreto = random.randint(1, 100)
intentos = 0
print("Adivina el número entre 1 y 100")


while True:
    try:
        opcion = int(input("Tu intento: "))
        intentos += 1


        if opcion< numero_secreto:
            print("Más alto")
        elif opcion > numero_secreto:
            print("Más bajo")
        else:

            print(f"Correcto Adivinaste en {intentos} intentos.")
            break

    except ValueError:
        print(" Error: Debes ingresar un número entero")1
        