pn= int(input("Ingrese numero: "))
sn= int(input("Ingrese numero: "))

if pn< sn:
    
    while pn<=sn:
        if pn%7==0:
            print(f"{pn} factor de 7")
        print(pn)
        pn+=1
else: 
    while pn>=sn:
        print(pn)
        pn-=1