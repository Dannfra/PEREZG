#modo funcion

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))


def num_medio(n1, n2, n3):
    if n1>n2: 
        if n1<n3:
                return "EL NUEMRO DEL MEDIO ES:",n1
        elif n2>n3:
                return "EL NUMERO DEL MEDIO ES:",n2
        else:
                return "EL NUMERO DEL MEDIO ES:",n3
    else:
          if n1>n3:
                return "EL NUMERO DEL MEDIO ES:",n1
          elif n2<n3:
                return "EL NUMERO DEL MEDIO ES:",n2
          else:
                return "EL NUMERO DEL MEDIO ES:",n3
print(num_medio(n1,n2,n3))