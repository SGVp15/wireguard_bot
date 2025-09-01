import json
import os
import re
import subprocess
from uuid import uuid4

import qrcode
import requests

from VPN_SERVICE import ABC_VPN_Service
from config import PATH_CONFIG, PATH_QR


class Xray(ABC_VPN_Service):
    def create_user_config(self, email) -> bool:
        # Read Xray config file
        config_path = "/usr/local/etc/xray/config.json"
        with open(config_path, 'r') as f:
            config = json.load(f)

        # Check if user already exists
        user_json = next(
            (client for client in config['inbounds'][0]['settings']['clients'] if client['email'] == email), None)

        if user_json:
            print("Пользователь с таким именем уже существует. Попробуйте снова.")
            return False

        # Generate new UUID
        uuid = str(uuid4())

        # Add new user to config
        new_client = {"email": email, "id": uuid, "flow": "xtls-rprx-vision"}
        config['inbounds'][0]['settings']['clients'].append(new_client)

        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        # Restart Xray service
        self.restart_service()

        # Get user index and configuration details
        clients = config['inbounds'][0]['settings']['clients']
        index = next(i for i, client in enumerate(clients) if client['email'] == email)
        protocol = config['inbounds'][0]['protocol']
        port = config['inbounds'][0]['port']
        uuid = clients[index]['id']

        # Read keys from file
        with open('/usr/local/etc/xray/.keys', 'r') as f:
            keys_content = f.read()
        pbk: str = re.search(r'Public [Kk]ey: (.*)', keys_content).group(1)
        sid: str = re.search(r'shortsid: (.*)', keys_content).group(1)

        # Get other configuration details
        username = clients[index]['email']
        sni = config['inbounds'][0]['streamSettings']['realitySettings']['serverNames'][0]

        # Get public IP
        ip = requests.get('https://icanhazip.com').text.strip()

        # Construct connection link
        link = (f"{protocol}://{uuid}@{ip}:{port}?security=reality&sni={sni}"
                f"&fp=firefox&pbk={pbk}&sid={sid}&spx=/&type=tcp"
                f"&flow=xtls-rprx-vision&encryption=none#{username}")
        # Print and save connection link
        full_path_conf_file = os.path.join(PATH_CONFIG, f'{email}.txt')
        with open(full_path_conf_file, 'w') as f:
            f.write(link)
        # Generate and display QR code
        qr = qrcode.QRCode(version=1, box_size=2, border=1)
        # qr = qrcode.make(data=link, version=1, box_size=2, border=1)
        qr.add_data(link)
        qr.make(fit=True)

        # Save QR code as PNG
        full_path_qr_file = os.path.join(PATH_QR, f'{email}.png')
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
        subprocess.run(['systemctl', 'restart', 'xray'], check=True)

    def stop_service(self):
        subprocess.run(['systemctl', 'stop', 'xray'], check=True)

    def get_user_config(self):
        pass

    def get_all_users_configs(self):
        pass

    def return_user_config(self):
        pass
