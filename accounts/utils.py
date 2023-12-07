import random
import string


def generate_account_number():
    letters = string.ascii_uppercase
    digits = ''.join(random.choice(string.digits) for _ in range(10))
    return '{}-{}'.format(''.join(random.choice(letters) for _ in range(2)),
                          digits)
