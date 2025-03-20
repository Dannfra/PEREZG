n = int(input("Ingrese el valor de N (mayor o igual a 1): "))

if n < 1:
    print(" Error: n debe ser mayor o igual a 1")
else:

    multiplos = [n for n in range(1, n + 1) if n % 5 == 0]

    if not multiplos:
        print(f"No hay múltiplos de 5 entre 1 y {n}")
    else:
        multiplos_texto = ", ".join(map(str, multiplos))