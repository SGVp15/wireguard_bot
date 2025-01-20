import os
import re

from config import PATH_CONFIG, PATH_KEYS, PATH_QR


class UserConfig:
    def __init__(self, file_name: str, s: str):
        with open(os.path.join(PATH_CONFIG, file_name), 'r') as f:
            s = f.read()
        self.name = file_name.replace('.conf', '')
        self.address = re.findall(r'Address\s*=\s*(.*)', s)[0].strip()

        with open(os.path.join(PATH_KEYS, f'{self.name}_public.key'), 'r') as f:
            self.public_key = f.read().strip()

    def rename_config(self, new_name):
        self.new_name = new_name
        os.rename(os.path.join(PATH_KEYS, f'{self.name}_public.key'),
                  os.path.join(PATH_KEYS, f'{self.new_name}_public.key'))
        os.rename(os.path.join(PATH_KEYS, f'{self.name}_private.key'),
                  os.path.join(PATH_KEYS, f'{self.new_name}_private.key'))
        os.rename(os.path.join(PATH_CONFIG, f'{self.name}.conf'),
                  os.path.join(PATH_CONFIG, f'{self.new_name}.conf'))
        os.rename(os.path.join(PATH_QR, f'{self.name}.png'),
                  os.path.join(PATH_QR, f'{self.new_name}.png'))
