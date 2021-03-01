import re


nameslist = input()
pattern = r'(\b[A-Z][a-z]+ [A-Z][a-z]+\b)'

matches = re.findall(pattern, nameslist)
print(' '.join(matches))
