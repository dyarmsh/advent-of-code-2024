import re

def calculate_product_extended(file_path):
    with open(file_path, "r") as file:
        chars_str = file.read()

    # Regex to capture all `mul()` instructions, `do()`, and `don't()`
    mul_pattern = re.compile(r"mul\((\d+),\s*(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    tokens = re.findall(r"mul\(\d+,\s*\d+\)|do\(\)|don't\(\)", chars_str)
    
    mul_enabled = True  # Default: `mul` instructions are enabled in the beginning
    total = 0

    for token in tokens:
        if do_pattern.match(token):  # Enable `mul`
            mul_enabled = True
        elif dont_pattern.match(token):  # Disable `mul`
            mul_enabled = False
        elif mul_pattern.match(token):  # Check if it's a `mul` call
            mul_match = mul_pattern.match(token)  
            if mul_match and mul_enabled:  # Process `mul` if enabled
                x, y = map(int, mul_match.groups())
                total += x * y

    return total

print(calculate_product_extended("day3/test.txt"))
print(calculate_product_extended("inputs/day3_input.txt"))
