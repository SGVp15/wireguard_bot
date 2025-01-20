import os
import re
import time
from datetime import datetime
from ipaddress import IPv4Network, IPv4Address
from os.path import isfile

from config import SERVER_IP, WG_DUMP, PATH_QR, PATH_CONFIG, WG_CONF, IPV4NETWORK, WG_SERVER_PORT, PATH_WG, PATH_KEYS, \
    WG_PRIVATE_KEY
from utils.log import log
from utils.translit import transliterate
from wireguard.user_config import UserConfig


class WIREGUARD:
    @staticmethod
    def create_user(name: str) -> (str, str):
        allowed_ips = '0.0.0.0/0'
        dns = '8.8.8.8'
        persistent_keepalive = 20
        net = IPv4Network(IPV4NETWORK)

        name = name.strip()
        name = re.sub(r'\s+', '_', name)
        name = transliterate(name) + datetime.today().strftime('_%Y-%m-%d')

        wg_public_key_file = os.path.join(PATH_WG, 'public.key')

        with open(WG_CONF, 'r') as f:
            s = f.read()

        # IP
        ips_current = [IPv4Address(x) for x in re.findall(r'(\d+\.\d+\.\d+\.\d+)', s)]

        ip = ''
        for ip_net in net.hosts():
            if ip_net not in ips_current:
                ip = ip_net
                break

        path_user_private_key = os.path.join(PATH_KEYS, f'{name}_private.key')
        path_user_public_key = os.path.join(PATH_KEYS, f'{name}_public.key')

        os.system(f'wg genkey | tee {path_user_private_key} | wg pubkey | tee {path_user_public_key}')
        time.sleep(0.1)

        with open(path_user_private_key) as f:
            private_key = f.read().strip()
        with open(path_user_public_key) as f:
            public_key = f.read().strip()

        s += f'\n' \
             f'[Peer] # {name}\n' \
             f'PublicKey = {public_key}\n' \
             f'AllowedIPs = {ip}/32\n'

        with open(WG_CONF, 'w') as f:
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
                        f'Endpoint = {SERVER_IP}:{WG_SERVER_PORT}\n' \
                        f'PersistentKeepalive = {persistent_keepalive}\n'

        time.sleep(0.1)
        full_path_conf_file = os.path.join(PATH_CONFIG, f'{name}.conf')
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

    @classmethod
    def create_wg_conf(cls):
        with open(WG_PRIVATE_KEY, 'r') as f:
            wg_private_key = f.read().strip()

        config_default = (f'[Interface]\n'
                          f'PrivateKey = {wg_private_key}\n'
                          f'Address = {IPV4NETWORK}\n'
                          f'ListenPort = {WG_SERVER_PORT}\n'
                          f'PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE\n'
                          f'PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o ens3 -j MASQUERADE\n')

        user_configs = [f for f in os.listdir(PATH_CONFIG) if isfile(f)]

        for file_name in user_configs:
            with open(os.path.join(PATH_CONFIG, file_name), 'r') as f:
                user_config = UserConfig(file_name, f.read())
                config_default += (f'\n[Peer]# {user_config.name}'
                                   f'PublicKey = {user_config.public_key}\n'
                                   f'AllowedIPs = {user_config.address}\n')

        with open(WG_CONF, 'w') as f:
            f.write(config_default)
