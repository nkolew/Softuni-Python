text = input()
emoticons = []
for i, c in enumerate(text):
    if c == ':':
        emoticons.append(text[i:i+2])

print('\n'.join(emoticons))