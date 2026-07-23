import csv

with open(
    "employees.csv",
    "w",
    newline = "") as file:

    writer = csv.writer(file)

    writer.writerow(["ID","Name","Domain","Salary"])
    writer.writerow(["1","Ram","Dev","500000"])
    writer.writerow(["2","Syam","Analatics","600000"])

print("CSV is created")



import csv

with open("employees.csv","r") as file:

  reader = csv.reader(file)

  for row in reader:
    print(row)


import csv

with open("employees.csv","a",newline="") as file:

  writer = csv.writer(file)

  writer.writerow([3,"Raju","Testing",560000])

print("Data is added successfully")


import csv

with open("employees.csv","r") as file:

  reader = csv.reader(file)

  next(reader)

  for row in reader:
    print(row[1],row[3])
