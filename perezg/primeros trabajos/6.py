#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa
print("escribir un numero del 0 al 9.999")
numero= int(input("numero deseado:"))
def numd(numero):
 if (numero<10):
        return"su numero cuenta con una cifra"
 else:
  if(numero>10 and numero<100):
        return"su numero cuenta con dos cifras"
  else:
   if(numero>100 and numero<1000):
        return"su numero cuenta con tres cifras"
   else:
    if(numero>1000 and numero<10000):
        return"su numero cuenta con cuatro cifras"
    else:
     if(numero>=10000):
        return"su numero cuenta con cinco cifras o mas"
print(numd(numero))