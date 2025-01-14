import os
import re
import time
from datetime import datetime
from ipaddress import IPv4Network, IPv4Address

from config import SERVER_IP, WG_DUMP, PATH_QR, PATH_CONFIG
from utils.log import log
from utils.translit import transliterate


class WIREGUARD:
    @staticmethod
    def create_user(name: str) -> (str, str):
        server_ip = SERVER_IP
        server_port = '443'

        allowed_ips = '0.0.0.0/0'
        dns = '8.8.8.8'
        persistent_keepalive = 20
        net = IPv4Network('172.26.10.0/24')

        name = name.strip()
        name = re.sub(r'\s+', '_', name)
        name = transliterate(name) + datetime.today().strftime('_%Y-%m-%d')

        PATH_WG = os.path.join('/', 'etc', 'wireguard')
        PATH_QR = os.path.join(PATH_WG, 'qr')

        wg_config_file = os.path.join(PATH_WG, 'wg0.conf')
        wg_public_key_file = os.path.join(PATH_WG, 'public.key')

        PATH_KEYS = os.path.join(PATH_WG, 'keys')
        PATH_CONFS = PATH_CONFIG
        os.makedirs(PATH_CONFS, exist_ok=True)
        os.makedirs(PATH_KEYS, exist_ok=True)

        with open(wg_config_file, 'r') as f:
            s = f.read()

        # IP
        ips_current = [IPv4Address(x) for x in re.findall(r'(\d+\.\d+\.\d+\.\d+)', s)]
        # print(ips_current)

        ip = ''
        for ip_net in net.hosts():
            if ip_net not in ips_current:
                ip = ip_net
                break
        # print(f'{ip=}')

        path_user_private_key = os.path.join(PATH_KEYS, f'{name}_private.key')
        path_user_public_key = os.path.join(PATH_KEYS, f'{name}_public.key')

        os.system(f'wg genkey | tee {path_user_private_key} | wg pubkey | tee {path_user_public_key}')
        time.sleep(0.1)

        with open(path_user_private_key) as f:
            private_key = f.read()
        with open(path_user_public_key) as f:
            public_key = f.read()

        s += f'\n\n' \
             f'[Peer]\n' \
             f'# {name}_public.key {public_key}' \
             f'PublicKey = {public_key}' \
             f'AllowedIPs = {ip}/32'

        with open(wg_config_file, 'w') as f:
            f.write(s)

        with open(wg_public_key_file) as f:
            wg_public_key = f.read()

        config_string = f'[Interface]\n' \
                        f'PrivateKey = {private_key}\n' \
                        f'Address = {ip}/32\n' \
                        f'DNS = {dns}\n' \
                        f'\n' \
                        f'[Peer]\n' \
                        f'PublicKey = {wg_public_key}\n' \
                        f'AllowedIPs = {allowed_ips}\n' \
                        f'Endpoint = {server_ip}:{server_port}\n' \
                        f'PersistentKeepalive = {persistent_keepalive}\n'

        print(config_string)
        time.sleep(0.1)
        full_path_conf_file = os.path.join(PATH_CONFS, f'{name}.conf')
        with open(full_path_conf_file, 'w') as f:
            f.write(config_string)

        WIREGUARD.restart_service()

        full_path_qr_file = os.path.join(PATH_QR, f'{name}.png')
        WIREGUARD.create_qr_code(input_file_path=full_path_conf_file, output_file_path=full_path_qr_file)

        return config_string, full_path_conf_file, full_path_qr_file

    @staticmethod
    def restart_service():
        os.system('systemctl restart wg-quick@wg0.service')
        log.info('[  OK  ] systemctl restart wg-quick@wg0.service')

    @staticmethod
    def create_all_qrcodes():
        for file in os.listdir(PATH_CONFIG):
            full_path_conf_file = os.path.join(PATH_CONFIG, file)
            qr = re.sub(r'\.conf$', '.png', file)
            full_path_qr_file = os.path.join(PATH_QR, qr)
            WIREGUARD.create_qr_code(input_file_path=full_path_conf_file, output_file_path=full_path_qr_file)

    @staticmethod
    def reboot_server():
        log.warning('[  OK  ] reboot')
        os.system('reboot')

    @staticmethod
    def create_qr_code(input_file_path, output_file_path):
        os.system(f'qrencode -t png -o {output_file_path} -r {input_file_path}')
        time.sleep(0.1)

    @staticmethod
    def get_dump():
        os.system(f'wg show wg0 dump > {WG_DUMP}')
        time.sleep(0.5)

    @classmethod
    def update_bot(cls):
        os.system('systemctl restart wg_bot')
