import os
import re

from config import PATH_CONFIG, PATH_KEYS, PATH_QR
from utils.log import log


class UserConfig:
    def __init__(self, file_name: str):
        self.name = file_name.replace('.conf', '')

        self.path_qr_file = os.path.join(PATH_QR, f'{self.name}.png')
        self.path_public_key = os.path.join(PATH_KEYS, f'{self.name}_public.key')
        self.path_private_key = os.path.join(PATH_KEYS, f'{self.name}_private.key')
        self.path_config_file = os.path.join(PATH_CONFIG, f'{self.name}.conf')

        self.address = ''
        self.public_key = ''
        if os.path.exists(self.path_config_file):
            with open(self.path_config_file, 'r') as f:
                s = f.read()
                self.address = re.findall(r'Address\s*=\s*(\d+\.\d+\.\d+\.\d+/\d+)', s)[0].strip()
        if os.path.exists(self.path_public_key):
            with open(self.path_public_key, 'r') as f:
                self.public_key = f.read().strip()

    def rename_conf(self, new_name):
        for path in (self.path_private_key, self.path_public_key, self.path_config_file, self.path_qr_file):
            dist = os.path.join(os.path.dirname(path), os.path.basename(path).replace(self.name, new_name))
            os.rename(path, dist)

    def delete_conf(self):
        for path in (self.path_private_key, self.path_public_key, self.path_config_file, self.path_qr_file):
            dist = os.path.join(os.path.dirname(path), 'trash', os.path.basename(path))
            try:
                os.renames(path, dist)
            except FileNotFoundError:
                log.error('FileNotFoundError', path)
