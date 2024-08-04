# version 1
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing name")
    self.name = name
    self.house = house
  ...

class Professor:
  def __init__(self, name, subject):
    if not name:
      raise ValueError("Missing name")
    self.name = name
    self.subject = subject
  ...

# version 2: inheritance
# defining another class with some common attributes
class Wizard:
  def __init__(self, name):
    if not name:
      raise ValueError("Missing name")
    self.name = name

class Student(Wizard):
  def __init__(self, name, house):
    super().__init__(name)
    self.house = house
  ...

class Professor(Wizard):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject
  ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")