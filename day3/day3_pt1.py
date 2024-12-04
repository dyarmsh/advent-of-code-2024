import re

def calculate_product(file_path):
    with open(file_path, "r") as file:
        chars_str = file.read()

    # Find all matches for the mul(x, y) pattern
    matches = re.findall(r"(mul\((\d+),\s*(\d+)\))", chars_str) # only captures the numbers
    total = 0 
    for x, y in matches:
        total += int(x) * int(y)

    return total 

print(calculate_product("day3/test.txt"))
print(calculate_product("inputs/day3_input.txt"))
