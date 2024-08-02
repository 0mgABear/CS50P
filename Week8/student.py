# version 1
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

# version 2
def main():
  name = get_name()
  house = get_house()
  print(f"{name} from {house}")

def get_name():
  return input("Name: ")

def get_house():
  return input("House: ")

if __name__ == "__main__":
  main()

# version 3
# using tuples and index
def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")

# can use dictionary - complex
# return multiple values?
# 1 tuple with 2 values
def get_student():
  name = input("Name: ")
  house = input("House: ")
  return (name, house)

# v 3.1
# using tuples and index
def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")

# can use dictionary - complex
# return multiple values?
# 1 tuple with 2 values
def get_student():
  name = input("Name: ")
  house = input("House: ")
  return [name, house]

# v 3.2
# using dictionary - better semantics
# don't have to memorise 0 and 1 - clearer and more expressive
def main():
  student = get_student()
  if student["name"] == "Padma":
    student['house'] == "Ravenclaw"
  print(f"{student['name']} from {student['house']}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return {"name": name, "house": house}

# version 4 - implementing classes

class Student:
  ...

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")


def get_student():
  student = Student() #creating an object of that class
  student.name = input("Name: ")
  student.house = input("House: ")
  return student


# v 4.2 - classes
# student blueprint - it will always have a name and house
# but we can pass in any name / house into the Class
class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house) # storing name and house within the empty Class instance / object

# v 4.3 - checking for presence of name and valid inputs
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house

# v 4.4 - with raising error and try-except
def get_student():
  name = input("Name: ")
  house = input("House: ")
  try:
    return Student(name, house)
  except ValueError:
    ...

# v 4.5 - with __str__
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house
  
  def __str__(self):
    return f"{self.name} from {self.house}"

# version 5 - creating more functionality
class Student:
  def __init__(self, name, house, patronus):
    if not name:
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house
    self.patronus = patronus
  
  def __str__(self):
    return f"{self.name} from {self.house}"
  
  def charm(self):
    match self.patronus: 
      case "Stag":
        return "🐎"
      case "Otter":
        return "🦦"
      case "Jack Russell terrier":
        return "🐕"
      case _:
        return "🗡️"

def get_student():
  name = input("Name: ")
  house = input("House: ")
  patronus = input("Patronus: ")
  try:
    return Student(name, house, patronus)
  except ValueError:
    ...

def main():
  student = get_student()
  print(student.charm())

# v 5.1 - version 5 still not very robust
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house
  
  def __str__(self):
    return f"{self.name} from {self.house}"
  
def get_student():
  name = input("Name: ")
  house = input("House: ")
  try:
    return Student(name, house)
  except ValueError:
    ...