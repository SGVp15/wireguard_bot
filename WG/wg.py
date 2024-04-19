import os
import re
import time
from datetime import datetime
from ipaddress import IPv4Network, IPv4Address

from config import SERVER_IP
from utils.translit import transliterate


def create_user(name):
    server_ip = SERVER_IP
    server_port = '443'

    allowed_ips = '0.0.0.0/0'
    dns = '8.8.8.8'
    persistent_keepalive = 20
    net = IPv4Network('172.26.10.0/24')

    name = name.strip()
    name = re.sub(r'\s+', '_', name)
    name = transliterate(name) + datetime.today().strftime('_%Y-%m-%d')

    wg_config_file = '/etc/wireguard/wg0.conf'

    path_wg = os.path.join('/', 'etc', 'wireguard')
    path_keys = os.path.join(path_wg, 'keys')
    path_confs = os.path.join(path_wg, 'confs')
    os.makedirs(path_confs, exist_ok=True)
    os.makedirs(path_keys, exist_ok=True)

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

    os.system(f'wg genkey | tee {path_keys}{name}_private.key | wg pubkey | tee {path_keys}{name}_public.key')
    time.sleep(0.1)

    with open(f'{path_keys}{name}_private.key') as f:
        private_key = f.read()
    with open(f'{path_keys}{name}_public.key') as f:
        public_key = f.read()

    s += f'\n\n' \
         f'[Peer]\n' \
         f'#{name}_public.key {public_key}' \
         f'PublicKey = {public_key}' \
         f'AllowedIPs = {ip}/32'

    with open(wg_config_file, 'w') as f:
        f.write(s)

    with open(f'{path_wg}public.key') as f:
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
    file = f'{path_confs}{name}.conf'
    with open(file, 'w') as f:
        f.write(config_string)

    print('[  START  ] systemctl restart wg-quick@wg0.service')
    os.system('systemctl restart wg-quick@wg0.service')
    print('[  OK  ] systemctl restart wg-quick@wg0.service')

    return config_string, file
