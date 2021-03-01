str = input()
capitals = []
for idx, chr in enumerate(str):
    if 65 <= ord(chr) <= 90:
        capitals.append(idx)
print(capitals)