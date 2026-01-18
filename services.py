import random
import string
import validators

def is_valid_url(url):
    return validators.url(url)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
