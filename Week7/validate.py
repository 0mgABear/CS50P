# version 1

email = input("What's your email? ").strip() #remove leading or trailing whitespace

#over-simplified
if "@" in email:
  print("Value")
else:
  print("Invalid")

# v 1.1
if "@" in email and "." in email:
  print("Value")
else:
  print("Invalid")

# v 1.2 - looking for the . in the domain name
username , domain = email.split("@")
if username and "." in domain:
  print("Valid")
else:
  print("Invalid")

# v 1.3 - even more precise
username , domain = email.split("@")
if username and domain.endswith(".edu"):
  print("Valid")
else:
  print("Invalid")

# version 2
import re
email = input("What's your email? ").strip() #remove leading or trailing whitespace

if re.search("@", email):
  print("Valid")
else:
  print("Invalid")

# v2.1
# something to the left, something to the right of @

if re.search(".+@.+", email):
  print("Valid")
else:
  print("Invalid")

# v2.2 if you could only use . and * without using +
if re.search("..*@..*", email):
  print("Valid")
else:
  print("Invalid")

# v2.3 - check for username, after username and domain, ends with .edu
if re.search(".+@.+.edu", email):
  print("Valid")
else:
  print("Invalid")

# we want it to literally be .edu, but the . in regex context is different - it means something else!
# . means any character!

# v2.4 - use escape character
# similar technique
# \ : special sequence 
# but we don't want python to misinterpret this as an escape sequence
# r: raw string - must use with \
if re.search(r".+@.+\.edu", email):
  print("Valid")
else:
  print("Invalid")

# version 3 - above doesn't check for sentences, doesn't check for multiple @'s
# no strict checking for the logic that it must start with username and end at .edu
if re.search(r"^.+@.+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# v3.1 - to ensure only 1@
# be even more restrictive
if re.search(r"^[^@]+@[^@]+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# v3.2 - v3.1 is too accommodating
# there is a certain format in the world for username
# say we only want alphabets in the username

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# v3.3 - using shortcuts
if re.search(r"^\w+@\w+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# v3.4 - to solve lower-case edu in v3.3 --> upper-case EDU will not work
# can convert input to lowercase using .lower()
# but if there's > 1 . after the @ - it would be invalid to

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")

# v3.5 - making a group and making that group optional
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")

# version 4
# regex used in reality
# simplified version - catches most errors but not all, not official
# browser-implemented
# just use a library instead.

regex_pattern = "^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
