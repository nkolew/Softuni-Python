import re


data = input()
pattern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'

matches =[]
for i in re.finditer(pattern, data):
    matches.append(i.group(0))
print(', '.join(matches)) 