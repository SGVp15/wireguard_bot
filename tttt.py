name = 'NAME'
public_key = 'PUBLIC_KEY'
ip = 'ip'
s = f'\n' \
     f'[Peer] # {name}\n' \
     f'PublicKey = {public_key}\n' \
     f'AllowedIPs = {ip}/32\n'
print(f'[{s}]')