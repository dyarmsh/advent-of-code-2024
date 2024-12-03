def how_many_safe(file_path):

    all_reports = []
    with open(file_path, "r") as file:
        for line in file:
            level = map(int, line.split())
            all_reports.append(list(level))
    
    num_safe_reports = 0

    # 1. Check if level's order is always increasing OR decreasing
    def is_monotonic(arr):
        return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))

    # 2. Check if difference is between 1-3 between consecutive elements
    def is_difference_between_1_and_3(arr):
        return all((1 <= abs(arr[i] - arr[i + 1]) <= 3) for i in range(len(arr) - 1))
    
    for level in all_reports:
        if is_monotonic(level) is True and \
        is_difference_between_1_and_3(level) is True:
            num_safe_reports += 1

    return num_safe_reports

print(how_many_safe("day_2/day_2_input.txt"))
