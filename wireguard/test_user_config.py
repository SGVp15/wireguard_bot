from unittest import TestCase

from wireguard.user_config import UserConfig


class TestUserConfig(TestCase):
    def test_create_config(self):
        s = '''[Interface]
PrivateKey = YNp/QGfYlVkgjfzL+PzpH85GjR1hN6igwGN/fk7nkVc=

Address = 172.26.10.3/32
DNS = 8.8.8.8

[Peer]
PublicKey = asShe7Ygc6pk98q9WKzVEpF4wz5hVsOvoVFYz424Z0I=

AllowedIPs = 0.0.0.0/0
Endpoint = 79.137.195.240:443
PersistentKeepalive = 20'''
        u = UserConfig('oololo.conf',s)
        print(f'{u.name=}\n{u.public_key=}\n{u.address=}\n')
