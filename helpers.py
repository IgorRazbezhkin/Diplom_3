import random
import string


def generate_random_email(domain="yandex.ru"):
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_part}@{domain}"

def generate_random_password(length=7):
    return ''.join(random.choices(string.digits, k=length))