import random
import string


def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(90))
