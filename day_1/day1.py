def determine_distance(file_path):

    lst1 = []
    lst2 = []

    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            lst1.append(left)
            lst2.append(right)

    lst1.sort()
    lst2.sort()

    total_distance = 0

    for i in range(len(lst1)):
        diff = abs(lst1[i] - lst2[i])
        total_distance += diff

    return total_distance

def determine_similarity_index(file_path):
    lst1 = []
    lst2 = []

    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            lst1.append(left)
            lst2.append(right)

    similarity_score = 0
    for i in range(len(lst1)):
        similarity_index = 0
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                 similarity_index += 1
        similarity_score += similarity_index * lst1[i]

    return similarity_score


# print(determine_distance("day1_input.txt"))
print(determine_similarity_index("day1_input.txt"))
