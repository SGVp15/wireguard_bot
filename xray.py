import json
import os
import re
import subprocess
from uuid import uuid4

import qrcode
import requests

from VPN_SERVICE import ABC_VPN_Service
from config import PATH_CONFIG, PATH_QR


import json
import uuid
import subprocess
import sys
import os
import socket


CONFIG_PATH = '/usr/local/etc/xray/config.json'


def get_server_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except: return "YOUR_IP"


def get_pub_key(priv_key):
    proc = subprocess.Popen(['/usr/local/bin/xray', 'x25519', '-i', priv_key],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate()
    for line in (out + err).split('\n'):
        if "Public key:" in line or "Password:" in line:
            return line.split(': ')[1].strip()
    return None

class Xray(ABC_VPN_Service):
    def create_user_config(self, email) -> bool:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)

        inbound = next(i for i in config['inbounds'] if i.get('tag') == 'VLESS-XHTTP-REALITY')
        new_uuid = str(uuid.uuid4())

        inbound['settings']['clients'].append({"id": new_uuid, "email": email, "level": 0})

        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)

        subprocess.run(['systemctl', 'restart', 'xray'])

        # Данные для ссылки
        ip = get_server_ip()
        reality = inbound['streamSettings']['realitySettings']
        xhttp = inbound['streamSettings']['xhttpSettings']
        pub_key = get_pub_key(reality['privateKey'])

        link = f"vless://{new_uuid}@{ip}:443?security=reality&sni={reality['serverNames'][0]}&fp=chrome&pbk={pub_key}&sid={reality['shortIds'][0]}&type=xhttp&mode={xhttp.get('mode', 'auto')}&path={xhttp['path'].replace('/', '%2F')}#{email}"

        # Generate and display QR code
        qr = qrcode.QRCode(version=1, box_size=2, border=1)
        # qr = qrcode.make(data=link, version=1, box_size=2, border=1)
        qr.add_data(link)
        qr.make(fit=True)

        # Save QR code as PNG
        full_path_qr_file = PATH_QR / f'{email}.png'
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(full_path_qr_file)
        return True

    def edit_user_config(self):
        pass

    def recreate_user_config(self):
        pass

    def remove_user_config(self):
        pass

    def get_status_service(self):
        pass

    def start_service(self):
        subprocess.run(['systemctl', 'start', 'xray'], check=True)

    def restart_service(self):
        self.stop_service()
        self.start_service()

    def stop_service(self):
        subprocess.run(['systemctl', 'stop', 'xray'], check=True)

    def get_user_config(self):
        pass

    def get_all_users_configs(self):
        pass

    def return_user_config(self):
        pass
