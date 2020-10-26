from crypto.crypto import Crypto


class Caesar(Crypto):
    def __init__(self, offset: int = 0):
        super().__init__(offset=offset)

    def encrypt(self, data: str) -> str:
        return ''.join([chr(ord(symbol) + self.offset) for symbol in data])

    def decrypt(self, data: str) -> str:
        return ''.join([chr(ord(symbol) - self.offset) for symbol in data])


if __name__ == '__main__':
    c = Caesar(offset=-2)
    text = 'my secret text'
    encrypted = c.encrypt(text)
    decrypted = c.decrypt(encrypted)
    print(text)
    print(encrypted)
    print(decrypted)
