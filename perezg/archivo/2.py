with open('ARCHIVOS/himno.txt','r') as file:              #logica valery
    contenido = file.read()
    palabra = 'bien'
    
contenido=contenido.split()
print(contenido)
repeticiones = [palabra for x in contenido if x == palabra.lower()]

print(repeticiones)
#palabras = contenido.lower().split()
#repeticiones = [palabra for palabra in palabras if palabra == palabra.lower()]

if repeticiones: 

    print(f'la palabra"{palabra}" se repite {len(repeticiones)} veces')
else:
    print(f'la palabra "{palabra}" no se encuentra en el archivo')