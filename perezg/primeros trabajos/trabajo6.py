count = 0
while True:
    num = int(input("Ingrese un número: "))
    if num == 0:
        break
    count += 1
    opuesto = -num
    print(f"El número {num} tiene como opuesto {opuesto}")
print(f"Se ingresaron {count} números.")