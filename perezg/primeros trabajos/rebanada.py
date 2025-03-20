
                                            #el primer elemento si se cuenta y el segundo no,

mylist = [10,8,6,4,2]
newlist = mylist[1:3]
print(newlist)

lista = [0,1,2,3,4,5,6,7,8,9]

rebanada = lista[-3:-1]
print(rebanada)

lista = [0,1,2,3,4,5,6,7,8,9]

rebanada = lista[-1:-8:2]    #primero inicio el segundo final y el tercero los pasos
print(rebanada)

#escriba una funcion que reciva una lista valor inicial y valor final extraiga la rebanada de la lista SI SE PUEDE HACER, en caso contrario emita un mensaje 
#escriba una funcion que reciba una lista  usando rebanadas halle el promedio de las dos mitades de la lista.si el tamaño de la lista es impar  añada un elemento al final que equivale al promedio.