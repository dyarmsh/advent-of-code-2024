import re

def calculate_product(file_path):
    with open(file_path, "r") as file:
        chars_str = file.read()

    matches = re.findall("mul\(\d+,\s*\d+\)", chars_str)

    num_pairs = []
    for i in matches:
        num_pairs.append(re.findall("\d+,\s*\d+", i)[0].split(","))

    total = 0
    for pair in num_pairs:
        total += int(pair[0]) * int(pair[1])

    return total

print(calculate_product("day3/test.txt"))
print(calculate_product("day3/day3_input.txt"))