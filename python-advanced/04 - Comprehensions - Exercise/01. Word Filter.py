def even_word(word):
    return len(word) % 2 == 0


text = input()

even_words = [word for word in text.split() if even_word(word)]

print('\n'.join(even_words))
