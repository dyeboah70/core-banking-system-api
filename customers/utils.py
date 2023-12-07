import random
import string
import re
from django.conf import settings


def generate_profile_id():
    """Generate a string like 'asac2323'."""
    letters = random.choices(string.ascii_lowercase, k=4)
    digits = random.choices(string.digits, k=4)
    return "".join(letters + digits)


def verify_ghana_card(ghana_card_number):
    GHANA_CARD_REGEX = settings.GHANA_CARD_REGEX
    if re.match(GHANA_CARD_REGEX, ghana_card_number):
        return True
    else:
        return False


def verify_phone_number(phone_number):
    PHONE_NUMBER_REGEX = settings.PHONE_NUMBER_REGEX
    if re.match(PHONE_NUMBER_REGEX, phone_number):
        return True
    else:
        return False
