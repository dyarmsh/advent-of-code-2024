def how_many_safe(file_path):

    all_reports = []
    with open(file_path, "r") as file:
        for line in file:
            level = map(int, line.split())
            all_reports.append(list(level))
    
    num_safe_reports = 0

    # 1. Check if level's order is always increasing OR decreasing
    order = ["increasing", "decreasing"]
    for level in all_reports:
        for l in range(1, len(level)+1):
            if level[l-1] < level[l]:
                if level_order == order[0] and l != 1:
                    level_order = order[0]
            elif level[l-1] > level[l]:
                level_order = order[1]
            else:
                break


    # 2. Check if difference is between 1-3 between consecutive elements

print(how_many_safe("day_2/test.txt"))
