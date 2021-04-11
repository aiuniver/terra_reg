import random
import string


def generate_prefix(length):
    char_range = string.ascii_letters + string.digits
    prefix = ''.join(random.sample(char_range, length))
    return prefix

