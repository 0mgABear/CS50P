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
