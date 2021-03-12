def decode_morse(morse_word: str) -> str:
    """Decode morse text, according to the problem description.

    Args:
        morse_word (str): The word to be decrypted.

    Returns:
        str: Decrypted word.
    """

    codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
             '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    morse_dict = {code: char for code, char in zip(codes, chars)}

    decoded_word = ''
    for code in morse_word.split():
        decoded_word += morse_dict[code]
    return decoded_word


data = input().split('|')
decoded_text = []
for morse_word in data:
    morse_word = morse_word.strip()
    decoded_text.append(decode_morse(morse_word))
print(' '.join(decoded_text))
