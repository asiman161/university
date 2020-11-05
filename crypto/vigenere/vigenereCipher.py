LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

from crypto.crypto import Crypto


class Vigenere(Crypto):
    def __init__(self, key: str = ""):
        super().__init__(key=key)

    def encrypt(self, text: str) -> str:
        return translate_message(self.key, text, 'e')

    def decrypt(self, text) -> str:
        return translate_message(self.key, text, 'd')


def translate_message(key, message, mode):
    translated = []  # Stores the encrypted/decrypted message string.

    key_index = 0
    key = key.upper()

    for symbol in message:  # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'e':
                num += LETTERS.find(key[key_index])  # Add if encrypting.
            else:
                num -= LETTERS.find(key[key_index])  # Subtract if decrypting.

            num %= len(LETTERS)  # Handle any wraparound.

            # Add the encrypted/decrypted symbol to the end of translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1  # Move to the next letter in the key.
            if key_index == len(key):
                key_index = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return ''.join(translated)


def main():
    # message = 'Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'
    # key = 'ASIMOV'
    # mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    message = input('\nEnter message: ')
    key = input("Encryption/decryption key: ")
    # key = getRandomKey()
    mode = input('Would you like to "encrypt" (e) or "decrypt" (d, default) this message? ')

    crypt = Vigenere(key)

    if mode == 'encrypt' or mode == 'e':
        translated = crypt.encrypt(message)
    else:
        translated = crypt.decrypt(message)

    mode = 'encrypt' if mode == 'encrypt' or 'e' else 'decrypt'
    print(f'sed message: {mode}')
    print(translated)
    print('')


if __name__ == '__main__':
    main()
