import random

def rebanadas(lista,ini,fin):
   
    if ini>len(lista)or fin<len(lista)*-1:
        return "fuera del rango de la lista"
    else:
        return lista[ini:fin]
def llenarlistarandom(lista):
    lista=[]
    cantidad=random.randint(5,20)
    num=0
    for i in range(cantidad):
        num=random.randint(5,20)
        while num in lista:
            num=random.randint(1,100)
        
        lista.append(num)
        return lista
    vector=[]
    vector=llenarlistarandom(vector)
    print(vector)
    reb1=rebanadas(vector,2,4)
    print(reb1)


