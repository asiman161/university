class Crypto:
    def __init__(self, key: str = "", offset: int = 0):
        self.key = key
        self.offset = offset

    def encrypt(self, data: str) -> str:
        if self.key != "":
            return data.upper()
        return data

    def decrypt(self, data: str) -> str:
        if self.key != "":
            return data.lower()
