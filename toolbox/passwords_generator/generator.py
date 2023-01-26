import random

number_list = list(range(10))
lower_list = [chr(i) for i in range(97, 97+26)]
upper_list = [chr(i) for i in range(65, 65+26)]

eisu = [chr(i) for i in range(97, 97+26)]
eisu.extend([chr(i) for i in range(65, 65+26)])
eisu.extend([chr(i) for i in range(48, 48+10)])
symbol_normal_list = [chr(i) for i in range(33, 127) if chr(i) not in eisu]


# 因みに「33」を「32」にすると半角空白が入る

def generator(count, number, upper, lower, symbol_normal, symbol_custom):
    dic = {}
    result = ""
    if number:
        dic["number"] = number_list
    if upper:
        dic["upper"] = upper_list
    if lower:
        dic["lower"] = lower_list
    if symbol_normal:
        dic["symbol_normal"] = symbol_normal_list
    if symbol_custom:
        dic["symbol_custom"] = list(symbol_custom)
    for i in range(count):
        key, item = random.choice(list(dic.items()))
        result += str(random.choice(item))
    return result
