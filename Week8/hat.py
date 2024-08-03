# sorting hat (harry potter)
# pass to the sorting hat the name - gives us the house the student should be in
import random

# version 1
class Hat:
  def __init__(self):
    self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  def sort(self, name):
    print(name, "is in", random.choice(self.houses))

hat = Hat() #instantiate a Hat object
hat.sort("Harry")

# improve such that we don't have to instantiate sorting hat
# there's only 1 sorting hat

# version 2 - with @classmethod
# no self - don't need / want multiple hats

class Hat:
  houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  def sort(cls, name):
    print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")