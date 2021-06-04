VOWELS = {'a', 'o', 'u', 'e', 'i'}
word = input()
print(''.join(c for c in word if c.lower() not in VOWELS))
