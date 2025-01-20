import re


class UserConfig:
    def __init__(self, filename: str, s: str):
        self.name = filename
        self.address = re.findall(r'Address\s*=\s*(.*)', s)[0].strip()
        self.public_key = re.findall(r'PublicKey\s*=\s*(.*)', s)[0].strip()

    def create_config(self):
        pass
