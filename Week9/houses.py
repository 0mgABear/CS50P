# version 1

students = [
{"name": "Hermione", "house": "Gryffindor"},
{"name": "Harry", "house": "Gryffindor"},
{"name": "Ron", "house": "Gryffindor"},
{"name": "Draco", "house": "Slytherin"},
{"name": "Padma", "house": "Ravenclaw"},]

houses= []
for student in students:
  if student ["house"] not in houses:
    houses.append(student["house"])

for house in sorted(houses):
  print(house)

# version 2 - changing the type of object used

students = [
{"name": "Hermione", "house": "Gryffindor"},
{"name": "Harry", "house": "Gryffindor"},
{"name": "Ron", "house": "Gryffindor"},
{"name": "Draco", "house": "Slytherin"},
{"name": "Padma", "house": "Ravenclaw"},]

houses= set()
for student in students:
  houses.add(student["house"]) #syntax is .add() for set

for house in sorted(houses):
  print(house)