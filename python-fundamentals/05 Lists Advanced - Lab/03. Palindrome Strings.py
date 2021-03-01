def palindromes_count(l: list, k: str):
    p_list = list(filter(lambda x: x == x[::-1], l))
    cnt = p_list.count(keyword)

    return (p_list, cnt)


wordlist = input().split()
keyword = input()

p_list, cnt = palindromes_count(wordlist, keyword)
print(f'{p_list}\nFound palindrome {cnt} times')
