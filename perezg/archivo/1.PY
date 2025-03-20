def palabra_himno(palabra):
    try:
        with open('ARCHIVOS/himno.txt', 'r',encoding='utf-8') as archivo:
            contenido = archivo.read().lower()
            ocurrencias = contenido.count(palabra.lower())
            if ocurrencias >0:
                print(f"tu palabra elegida {palabra}aparece {ocurrencias} veces en el himno de colombia")
            else:
                print(f"Tu palabra {palabra} no esta en el himno de colombia")    
    except FileNotFoundError:
        print("El archivo 'himno.txt' no se encuentra en el directorio.")                 
palabra = input("Que palabra desea buscar: ")
palabra_himno(palabra)
 



