from itertools import repeat, chain
from random import choice, randrange, shuffle

from .enums import CharTypeEnum

DIGITS_COUNT = 10
LETTERS_COUNT = 26
SPECIAL_CHARS = '!@#$~%^&*()-+=_[]`:;"\'|\\/?.,<>{}'
SPECIAL_CHARS_COUNT = len(SPECIAL_CHARS)


def get_generator(start_char, idx_range):
    start_idx = ord(start_char)

    def generator():
        return chr(start_idx + randrange(idx_range))

    return generator


generate_digit = get_generator('0', DIGITS_COUNT)
generate_up_letter = get_generator('A', LETTERS_COUNT)
generate_low_letter = get_generator('a', LETTERS_COUNT)


def generate_special_char():
    return choice(SPECIAL_CHARS)


GENERATOR_MAP = dict(zip(CharTypeEnum, (
    generate_digit,
    generate_up_letter,
    generate_low_letter,
    generate_special_char,
)))


def generate_password(
        length=12,
        digits_min_count=1,
        up_letters_min_count=1,
        low_leters_min_count=1,
        special_min_count=1):
    char_types_map = {
        type_: count
        for type_, count in zip(
            CharTypeEnum,
            (
                digits_min_count,
                up_letters_min_count,
                low_leters_min_count,
                special_min_count,
            )
        ) if count > 0
    }

    using_types = tuple(char_types_map.keys())

    template = list(chain.from_iterable((
        repeat(type_, count)
        for type_, count in char_types_map.items()
    )))

    template.extend((
        choice(using_types)
        for i in range(length - len(template))
    ))

    shuffle(template)

    return ''.join(
        GENERATOR_MAP[type_]()
        for type_ in template
    )
