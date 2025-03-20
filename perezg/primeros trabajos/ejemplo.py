def opuesto():
    n=1
    c=0
    s=0
    while n!=0:
        n=int(input("ingrese numero"))
        print (n*-1)
        c+=1
        s=s+n
    return c-1,"la suma de los numeros ingresados es: ",s


    