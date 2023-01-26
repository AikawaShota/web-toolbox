import random

number_list = list(range(10))
lower_list = [chr(i) for i in range(97, 97+26)]
upper_list = [chr(i) for i in range(65, 65+26)]

eisu = [chr(i) for i in range(97, 97+26)]
eisu.extend([chr(i) for i in range(65, 65+26)])
eisu.extend([chr(i) for i in range(48, 48+10)])
symbol_normal_list = [chr(i) for i in range(33, 127) if chr(i) not in eisu]


def generator(count, number, upper, lower, symbol_normal, symbol_custom):
    character_list = []
    result = ""
    if number:
        character_list.extend(number_list)
    if upper:
        character_list.extend(upper_list)
    if lower:
        character_list.extend(lower_list)
    if symbol_normal:
        character_list.extend(symbol_normal_list)
    if symbol_custom:
        character_list.extend(list(symbol_custom))
    for i in range(count):
        result += str(random.choice(character_list))
    return result
