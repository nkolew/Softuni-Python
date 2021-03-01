def caesar(text: str):
    result = ''
    for c in text:
        result += chr(ord(c)+3)
    return result

text = input()
print(caesar(text))
    