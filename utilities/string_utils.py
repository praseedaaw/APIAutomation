import string
import random


def unique_string(size=10, chars=string.ascii_lowercase + string.digits):
    # Utility function returns a unique string
    return ''.join(random.choice(chars) for _ in range(size))
