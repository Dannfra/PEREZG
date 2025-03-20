import json
with open("C:/Users/Aprendiz/Documents/perezg/archivo/employees.json",'r') as eljson:
    data=json.load(eljson)
    sal=[x for x in data]
 
    lista=[int(i["SALARY"])for i in sal[1:]]
    print (lista)
    total=0
    
    for c in sal:
        total=total+c
        prom=total/len(lista)
    print(prom)
  

"""
for element in data:
    print(element(int['SALARY']))
    print("_"*20)
"""
