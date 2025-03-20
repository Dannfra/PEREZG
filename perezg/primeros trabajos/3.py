1
def pedir_numero():
    while True:
        try:
            return int(input("Ingresa un número: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def imprimir_opuesto(num):
    print(f"{num} opuesto es {-num}")

def contar():
    contador = 0

    while True:
        num = pedir_numero()
        if num == 0:
            break

        imprimir_opuesto(num)
        contador 1+1
        
        
    1
    
        
    
    print(f"Se ingresaron {contador} números.")

contar()ef pedir_numero():
    return int(input("Ingresa un número: "))

def imprimir_opuesto(num):
    print(f"{num} opuesto {-num}")

def contar():
    contador = 0

    while True:
        num = pedir_numero()
        if num ==0:
            break

        imprimir_opuesto(num)
        contador += 1
    
    print(f"se ingresaron {contador}numeros:")

contar()