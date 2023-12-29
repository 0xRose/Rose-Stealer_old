import string
import random


def get_random_string(length):
    letters = string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str
