import random
import string


def create_password(len_password=20) -> str:
    s = ''
    s += string.ascii_lowercase
    s += string.ascii_uppercase
    s += string.digits
    symbols = list(s)
    password = ''.join(random.sample(symbols, len_password))
    return password
