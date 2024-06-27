print("hello world")

name = input("What's your name? ")
print("Hello,", name)
# print("Hello, " + name) - another way to do the same thing

print(f"Hello, {name}")

# Creating your own function to say hello

def hello(name):
  print("Hello,", name)
