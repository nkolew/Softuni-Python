def hide_words(banned_words: list, text: str):
    for word in banned_words:
        while word in text:
            text = text.replace(word, '*'*len(word))
    return text


banned_words = input().split(', ')
text = input()

print(hide_words(banned_words, text))
