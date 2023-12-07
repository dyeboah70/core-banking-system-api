import random
import string


def generate_transaction_reference(name):
    initials = ''.join(word[0].upper() for word in name.split())
    random_number = ''.join(random.choice(string.digits) for _ in range(4))
    transaction_reference = f"{initials}-{random_number}"
    return transaction_reference

# Example usage
# name = "Bruce Lee"
# reference_number = generate_transaction_reference(name)
# print(reference_number)
