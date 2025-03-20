
import csv
with open("") as mydata:
    data=csv.reader(mydata)
    for x in data:
        print(x[2])
    