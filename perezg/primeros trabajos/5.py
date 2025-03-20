print("escribe 3 numeros")
n1=int(input("primer numero"))
n2=int(input("segundo numero"))
n3=int(input("tercer numero"))
def comp_num(n1, n2, n3):
 if(n1>n2 and n1<n3)or(n1<n2 and n1>n3):
    return("los numeros son distintos")
 else:
    if(n2>n1 and n2<n3)or(n2>n3 and n2<n1):
                                      return"los numeros son distintos"
    else:
     if(n3>n1 and n3<n2)or(n3>n2 and n3<n1):
                                      return"los numeros son distintos"
     else:
            if(n1==n2==n3):
                                      return"los numeros son iguales"
            else:
                      if(n1==n2) or (n1==n3) or (n3==n2):
                                      return"hay 2 numeros iguales en este momento"
    
print (comp_num(n1,n2,n3))