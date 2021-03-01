a = input()
print(''.join(list(reversed(a))))


def reversed_word_func():
    """
    Reverses the word
    Input: Reads console string
    Output: Prints reversed string on console
    """
    word = input()
    reversed_word = ''

    for idx in range(len(word)-1, -1, -1):
        reversed_word += word[idx]
    print(reversed_word)


reversed_word_func()


a = input()
print(a[::-1])
