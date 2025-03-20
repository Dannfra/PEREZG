lista=[]


for i in range(11):
    lista.append(i*10)
    
    print(lista)
    
    
def llenar_lista(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=int(input("ingrese numero: "))
        lista.append(num)  #voy a meterle datos a una lista
    return lista

vector=[]
vector=llenar_lista(vector,5)
print(vector)
    
    
    
# llenar_lista(lista,5)  #esta linea va a continuar domnde quedo la lista
# print("_"*20)
# llenar_lista(10)
# print("_"*20)
# llenar_lista(20)
