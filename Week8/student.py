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

class Student:
  def __init__(self):

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")


def get_student():
  name = input("Name: ")
  house = input("House: ")
  student = Student(name, house)
  return student