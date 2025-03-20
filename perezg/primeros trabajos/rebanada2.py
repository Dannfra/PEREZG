
def mitades(lista):
    tam=len(lista)
    print(tam)
    if tam%2!=0:
        m=media(lista)
        lista.append(int(m))
        tam=len(lista)
        r1=lista[:int(tam/2)]
        r2=lista[int(tam/2):]
        print(f"media1={r1}")
        print(f"media2={r2}")
        
    