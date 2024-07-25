name = input("What's your name? ")


# version 1 file = open("names.txt", "w") 
file = open('names.txt', 'a') # a - for appending
file.write(f"{name}\n") # for new row
file.close()

# version 2 , using with
with open("names.txt", "a") as file:
  file.write(f"{name}\n")

# version 3, to read files
with open('names.txt', "r") as file:
  lines = file.readlines()

# v3.1
for line in lines:
  print('hello,', line, end='') # to not create a new line

# v3.2 
for line in lines:
  print('hello,', line.rstrip())

# version 4
with open('names.txt', "r") as file:
  for line in file:
    print("hello,", line.rstrip())

# version 5 - say you want to sort, cannot go line by line
# too late to sort if you're already accessing each line
# common technique when dealing with files / information (generally)
# when you want to change the data in some way (e.g. sorting)
# create a variable at the top (e.g. list), adding/appending information to it in one place - just to collect it, and then do something afterwards

names = []
with open('names.txt') as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):
  print(f"hello, {name}")

# v5.1 - sorting the file directly
with open('names.txt') as file:
  for line in sorted(file):
    print("hello,", line.rstrip())