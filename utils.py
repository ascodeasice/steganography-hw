import random

from texts import texts


def get_random_char():
    return random.choice(texts)


def remove_if_in(arr, remove_items):
    new_list = [x for x in arr if x not in remove_items]
    return new_list
