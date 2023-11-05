import re

pattern = r"\d{3}-\d{2}-\d{4}"

text = "gsfdgfdsg 425-75-4532 vdbvcb 421-45-7541 "

found = re.findall(pattern, text)

if found:
    print("Pattern found:", found)
else:
    print("Pattern not found")