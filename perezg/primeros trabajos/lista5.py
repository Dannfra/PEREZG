import random
lista=[i for i in range(5)]   # variable estructura constante ( el elemento es el que esta de primero) es el que llena la lista(con lo que se va a llenar)
print(lista)
lista=[i*i for i in range(1,6)]
print(lista)

lista=[random.randint(0,100) for i in range(random.randint(5,20))]
print(lista)


# se va allenar con 0 si se cumple esta condicion de lo contrario con x la cual es un elemento que esta en la otra lista
lista3=[0 if x%2==0 else x for x in lista]


# si el numero es menor que 50 usted llena la lista con 1 pero si es mayor que 50 se pone 2 - si es par entonces doblelo si e simpar halle la mitad 

lista4=[1 if  x< 50 else 2 for x in lista]
print(f"lista4={lista4}")

lista5=[x*2 if x%2==0 else x/2 for x in lista]
print(f"lista5={lista5}")