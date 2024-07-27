with open('students.csv') as file:
  for line in file:
    row = line.rstip().split(',')
    print(f"{row[0]} is in {row[1]}")

#version 2
with open('students.csv') as file:
  for line in file:
    name, house = line.rstip().split(',')
    print(f"{name} is in {house}")

#version 3
students = []

with open('students.csv') as file:
   for line in file:
    name, house = line.rstrip().split(',')
    students.append(f"{name} is in {house}")

for student in sorted(students):
  print(student)

#version 4 - better technique to sort by name, not by English / luck
students = []

with open('students.csv') as file:
   for line in file:
    name, house = line.rstrip().split(',')
    student = {"name": name, "house": house}
    students.append(student)

for student in students:
  print(f"{student['name']} is in {student['house']}")

# list of dictionaries - unsorted

# v4.1
def get_name(student):
  return student['name']

for student in sorted(students, key=get_name):
  print(f"{student['name']} is in {student['house']}")

# version 5 - incorporating csv

import csv 

students = []

with open('students.csv') as file:
  reader = csv.reader(file)
  for name, home in reader: #destructuring!
    students.append({"name": name, "home": home}) 

for student in students:
  print(f"{student['name']} is from {student['home']}")

# v 5.1 - DictReader

students = []

with open('students.csv') as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name": row["name"], "home": row["home"]}) #coding defensively - in case changes to CSV file

for student in students:
  print(f"{student['name']} is from {student['home']}")

# version 6 - writing a CSV (instead of just reading)

import csv
name = input("What's your name? ")
home = input("What's your home? ")

with open('students.csv', "a") as file:
  writer = csv.writer(file)
  writer.writerow([name, home])

# v 6.1 - DictWriter - without precisely worrying about the order
import csv
name = input("What's your name? ")
home = input("What's your home? ")

with open('students.csv', "a") as file:
  writer = csv.DictWriter(file, fieldnames=['name', 'home'])
  writer.writerow({"name": name, "home": home})