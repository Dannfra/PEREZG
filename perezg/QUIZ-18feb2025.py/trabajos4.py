numero = int(input("Ingrese un número entre 0 y 9999: "))

if numero < 0 or numero > 9999:
    print(" Error: El número excede los límites permitidos")
else:
    cantidad_cifras = len(str(numero))

    if cantidad_cifras == 1:
        mensaje = "tiene 1 cifra"
    else:
        mensaje = f"tiene {cantidad_cifras} cifras"

    print(f"El número {mensaje}")
    