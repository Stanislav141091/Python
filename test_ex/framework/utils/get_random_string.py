import random
import string


def get_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.sample(letters, length))
    return random_string