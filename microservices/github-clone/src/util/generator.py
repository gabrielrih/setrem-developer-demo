import string
import random


def generate_random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
