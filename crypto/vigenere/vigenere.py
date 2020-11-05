from crypto.crypto import Crypto


class Vigenere(Crypto):
    def __init__(self, key: str = ""):
        super().__init__(key=key)

    def encrypt(self, text: str) -> str:
        key = self.key * (len(text) // len(self.key) + 1)
        encrypted = ""
        for i, v in enumerate(text):
            code = ord(v) + ord(key[i]) - 64  # - 64 это для коррекции нижнего регистра. для большого удалить
            encrypted += chr(code % 26 + ord('a'))
        return encrypted

    def decrypt(self, text) -> str:
        key = self.key * (len(text) // len(self.key) + 1)
        decrypted = ''
        for i, j in enumerate(text):
            code = ord(j) - ord(key[i])
            decrypted += chr(code % 26 + ord('a'))
        return decrypted


def start():
    v = Vigenere(key="key")
    text = 'hello'
    encrypted = v.encrypt(text)
    decrypted = v.decrypt(encrypted)
    print(text)
    print(encrypted)
    print(decrypted)


if __name__ == '__main__':
    start()
