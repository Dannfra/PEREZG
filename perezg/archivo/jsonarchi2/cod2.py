import json
import csv
with open("C:/Users/Aprendiz/Documents/perezg/archivo/employees.json",'r') as eljson:
    data=json.load(eljson)
    
headers=data[0].keys()

with open("C:/Users/Aprendiz/Documents/perezg/archivo/employees.json",'w') as elcsv:
    data=json.load(elcsv)
    writer=csv.Dicwrite(elcsv,headers)
    writer.writerows()
    writer.writerows(data)