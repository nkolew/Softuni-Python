def substring_replace(substring: str, string: str):
    while substring in string:
        string = string.replace(substring, '')
    return string


substring = input()
string = input()

print(substring_replace(substring, string))
