oficina={
    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100
 }



def nuevaclave(ofi, clave,valor):
    for key in ofi.keys():
        if key!=clave:
            return("la clave ya existe")
        
            
         
    else:
        ofi[clave]=valor


    return ofi
    
    
   
miclave=input("ingrese la nueva clave")   
clave =input("ingresa la nueva clave")
valor=input("")
nuevaclave(oficina, miclave,)