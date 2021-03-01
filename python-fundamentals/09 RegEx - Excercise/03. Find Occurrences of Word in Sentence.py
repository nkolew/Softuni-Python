import re

data = input()
searched = input()

pattern = fr'(?i)\b{searched}\b'

result = re.findall(pattern, data)
print(len(result))
