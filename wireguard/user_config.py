import os
import re

from config import PATH_CONFIG, PATH_KEYS, PATH_QR


class UserConfig:
    def __init__(self, file_name: str):
        self.name = file_name.replace('.conf', '')

        self.path_qr_file = os.path.join(PATH_QR, f'{self.name}.png')
        self.public_key = os.path.join(PATH_KEYS, f'{self.name}_public.key')
        self.private_key = os.path.join(PATH_KEYS, f'{self.name}_private.key')
        self.config_file = os.path.join(PATH_CONFIG, f'{self.name}.conf')

        with open(self.config_file, 'r') as f:
            s = f.read()
            self.address = re.findall(r'Address\s*=\s*(\d+\.\d+\.\d+\.\d+/\d+)', s)[0].strip()

        with open(self.public_key, 'r') as f:
            self.public_key = re.sub('\s+', '', f.read())

    def rename_config(self, new_name):
        for path in (self.public_key, self.public_key, self.config_file, self.path_qr_file):
            dist = os.path.join(os.path.dirname(path), os.path.basename(path).replace(self.name, new_name))
            os.rename(path, dist)
