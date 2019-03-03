from enum import IntEnum, auto


class CharTypeEnum(IntEnum):
    NUMBER = auto()
    UP_LETTER = auto()
    LOW_LETTER = auto()
    SPECIAL_CHAR = auto()
    ANY_CHAR = auto()
