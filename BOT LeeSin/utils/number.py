def roman_to_int(num: str) -> int:
    roman_num = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5
    }
    return roman_num[num]