def decipher(l: list):
    word_list = []
    for word in l:
        nums = []
        letters = []
        for let in word:
            if let.isdigit():
                nums.append(int(let))
            elif let.isalpha():
                letters.append(let)
        num = int(''.join(map(str, nums)))
        f_let = chr(num)
        letters[0], letters[-1] = letters[-1], letters[0]
        letters.insert(0, f_let)
        word_list.append(''.join(letters))

    return ' '.join(word_list)


msg = input().split()

print(decipher(msg))
