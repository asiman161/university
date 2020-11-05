from crypto.crypto import Crypto


# гаммирование с помощью XOR
# описание в README.md
class Gamma(Crypto):
    def __init__(self, key: str = ""):
        super().__init__(key=key)

    def encrypt(self, text: str) -> str:
        key = self.__increase_key(text)
        pairs = zip(list(text), list(key))

        return ''.join([chr(ord(x[0]) ^ ord(x[1])) for x in pairs])

    def decrypt(self, text) -> str:
        return self.encrypt(text)

    def __increase_key(self, text) -> str:
        return self.key * (len(text) // len(self.key) + 1)


def start():
    g = Gamma("hello super key")
    encrypted = g.encrypt("super big world with some random messages")
    decrypted = g.decrypt(encrypted)
    print(f"encrypted: {encrypted}")
    print(f"decrypted: {decrypted}")


if __name__ == "__main__":
    start()
