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
    
    def is_safe_with_1_removal(arr):
        # [ 1 3 2 4 5 ] 0:
        arr_to_check = arr

        # first check if removing first element helps
        sub_array = arr[1:len(arr_to_check) + 1]
        if is_safe_without_removals(sub_array) is True:
            return True
        else:
            for i in range(1, len(arr)):
                sub_array = arr[0:i+1]
                if is_safe_without_removals(sub_array) is False:
                    arr_to_check.pop(i)
                    if is_safe_without_removals(arr_to_check) is True:
                        return True
                    else:
                        return False

    def is_safe_without_removals(arr):
        if is_monotonic(arr) is True and \
        is_difference_between_1_and_3(arr) is True:
            return True
        return False
        
    # safe_arrays = []
    for level in all_reports:
        if is_safe_without_removals(level) or is_safe_with_1_removal(level):
            # safe_arrays.append(level)
            num_safe_reports += 1

    # print(safe_arrays)
    return num_safe_reports

   
print(how_many_safe("day_2/test.txt"))
print(how_many_safe("day_2/day_2_input.txt"))
