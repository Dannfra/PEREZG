import random



conjunto={1}
print(type(conjunto))
conjunto2=set([1,2,3])
lista=[random.randint(1,10)for i in range(15)]
print(lista)
print(type(lista))
conjunto3=set(lista)
print(type(conjunto3))
print(conjunto3)

conjunto.update(lista)
print(f"conjuntop despues de update")
print(f"{conjunto}")
