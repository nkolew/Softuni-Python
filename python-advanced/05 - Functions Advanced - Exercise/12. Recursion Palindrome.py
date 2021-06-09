def palindrome(word, index):
    r_index = len(word) - 1 - index
    l_chr = word[index]
    r_chr = word[r_index]
    if l_chr != r_chr:
        return f'{word} is not a palindrome'
    if index >= r_index:
        return f'{word} is a palindrome'
    return palindrome(word, index+1)
