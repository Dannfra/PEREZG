import random
def crear(lista,cantidad):
    lista=[]
    for x in range (cantidad):
        x=random.randint(5,20)
        lista.append(x)
    return lista
vec=[]
tam=int(input("Cuantos numeros ingreso a la lista: "))
vec=crear(vec,tam)
print(vec)
def sumar(vec):
    suma=0
    for i in vec:
        suma += i
    return suma

def promedio(vec):
    suma=0
    for i in vec:
        suma += i
    promedio=suma / len(vec)
    return promedio 

def mayor(vec):
    mayor = max(vec)
    return mayor

def menor(vec):
    menor = min(vec)
    return menor 


def ascendente(vec):
    inter=True
    while inter:
        inter = False
        for i in range(len(vec)-1):
            if vec[i]>vec[i+1]:
                inter=True
                vec[i],vec[i+1]=vec[i+1],vec[i]
                return vec
        
def mediana(vec):  
    if len(vec)%2 == 0:
        ascendente(vec)
        mediana = (vec[len(vec)//2-1] +  vec[len(vec)//2]/2	)
    else:
        ascendente()
        mediana = [len(vec)//2]
    return mediana
    
 
sel=1
while sel !=5:
    print("1-sumar")
    print("2-promedio")
    print("3-mayor")
    print("4-menor")
    print("5-ascendente")
    print("6-mediana")
    print("8-salir")

    sel=int(input("Seleccione Opción: "))

    match sel:
        case 1:
            print(sumar(vec))
        case 2:
            print(promedio(vec))
        case 3:
            print(mayor(vec))
        case 4:
            print(menor(vec))
        case 5:
            print(ascendente(vec))   
        case 6:
            print(mediana(vec))
        case 8:
            break
        case _:
            print("Opción Equiviocada")