from collections import defaultdict

synonyms = defaultdict(list)

n = int(input())
for _ in range(n):
    word = input()
    synonym = input()
    synonyms[word].append(synonym)

for word in synonyms:
    print(f'{word} - {", ".join(synonyms[word])}')
