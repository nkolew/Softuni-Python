from collections import deque


class EncryptionGenerator:
    text: str
    MIN_CHAR = 32
    MAX_CHAR = 126

    def __init__(self, text: str) -> None:
        self.text = text

    def __add__(self, n: int) -> str:
        if not isinstance(n, int):
            raise ValueError('You must add a number.')

        chars = deque(self.text)
        encrypted_message = []
        while chars:
            c = chars.popleft()
            enc_c = ord(c) + n
            if enc_c < self.__class__.MIN_CHAR:
                enc_c += 95
            elif enc_c > self.__class__.MAX_CHAR:
                enc_c -= 95
            encrypted_message.append(chr(enc_c))

        return ''.join(encrypted_message)


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
