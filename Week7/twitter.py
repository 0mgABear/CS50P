# prompt user for url of their twitter profile
# extract from it and infer what is their username
import re

# Version 1 - fragile
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# v1.1
# http, no https, www,  no / , ? - all will break the code
username = re.sub("https://twitter.com/", "", url)
print(f"Username: {username}")
# issues as stated below:
# protocols
# phrase
# the . allows for any character without a \

# v1.2 - simplest way of accepting either http , https
# ? behind s
# www - group and optional
# making protocol optional too
username = re.sub("^(https?://)?(www\.)?twitter.com/", "", url)
print(f"Username: {username}")

# version 2 - going back to re.search
# using () to capture the information
# re.search returns an answer
if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
  print(f'Username: ', matches.group(2))

# v2.1 - 2nd iteration and improvement
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
  print(f'Username: ', matches.group(1))

# v2.2 - final iteration
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
  print(f'Username: ', matches.group(1))