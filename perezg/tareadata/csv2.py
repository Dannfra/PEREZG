import csv

def obtener_salarios(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        empleados = []
        for row in reader:
            try:
                salario = float(row["SALARY"])
                empleados.append({"first_name": row["FIRST_NAME"], "last_name": row["LAST_NAME"], "salary": salario})
            except ValueError:
                continue
        
        empleados = sorted(empleados, key=lambda x: x["salary"])  # Ordenar por salario
        top_7 = empleados[:7]  # Obtener los 7 con salario más bajo
        
        return top_7

def main():
    archivo = "employees.csv"  # Cambia esto por la ruta real de tu archivo
    top_7 = obtener_salarios(archivo)
    print("Los 7 empleados con salario más bajo:")
    for emp in top_7:
        print(f"{emp['first_name']} {emp['last_name']} - ${emp['salary']}")

if __name__ == "__main__":
    main()
