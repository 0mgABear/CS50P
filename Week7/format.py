#reformat user input in the way we expect / want
import re

name = input("what's your name? ").strip()

# version 1
# inherently fragile/flawed logic
# .split() does not recognise REGEX, need to use re library

if "," in name:
  last, first = name.split(", ")
  name = f"{first} {last}"

# version 2
# using () for capturing purposes
matches = re.search(r"^(.+), (.+)$", name)
if matches:
  last, first = matches.groups()
  name = f"{first} {last}"

# v2.1 without using matches.groups()
# there is something else in position 0 - we don't use
matches = re.search(r"^(.+), (.+)$", name)
if matches:
  name = matches.group(2) + " " + matches.group(1)

# v2.2 - making the space optional
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
  name = matches.group(2) + " " + matches.group(1)

# version 3 - tightening things up
# using walrus operator
if matches := re.search(r"^(.+), ?(.+)$", name):
  name = matches.group(2) + " " + matches.group(1)


print(f"hello, {name}")