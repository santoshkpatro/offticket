from django.utils.crypto import get_random_string


def generate_user_id():
    return get_random_string(10).upper()