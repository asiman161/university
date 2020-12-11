from crypto.crypto import Crypto


class SimpleReplace(Crypto):
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    encrypt_map = dict()
    decrypt_map = dict()

    def __init__(self, key: str):
        if len(key) != len(self.alphabet):
            raise ValueError(f"the len of key must be {len(self.alphabet)}. provided key len is {len(key)}")
        super().__init__(key=key)
        zipped = zip(self.alphabet, self.key)
        for v in zipped:
            self.encrypt_map[v[0]] = v[1]
            self.decrypt_map[v[1]] = v[0]

    def encrypt(self, data: str) -> str:
        return ''.join([self.encrypt_map[symbol] for symbol in data])

    def decrypt(self, data: str) -> str:
        return ''.join([self.decrypt_map[symbol] for symbol in data])


if __name__ == '__main__':
    sr = SimpleReplace(' qwertyuiopasdfghjklzxcvbnm')
    text = 'secret long message'
    encrypted = sr.encrypt(text)
    decrypted = sr.decrypt(encrypted)
    print(text)
    print(encrypted)
    print(decrypted)
