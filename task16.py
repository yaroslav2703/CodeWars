def sum_pairs(ints, s):
    sum_list = []
    for i in range(0, len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                sum_list.append([ints[i], i, ints[j], j])
    if len(sum_list) == 1:
        return [sum_list[0][0], sum_list[0][2]]
    elif len(sum_list) == 0:
        return None
    else:
        finish = sum_list[0]
        for i in sum_list:
            if i[3] < finish[3]:
                finish = i
        return [finish[0], finish[2]]


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

print(sum_pairs(l1, 8))
print(sum_pairs(l2, -6))
print(sum_pairs(l3, -7))
print(sum_pairs(l4, 2))
print(sum_pairs(l5, 10))
print(sum_pairs(l6, 8))
print(sum_pairs(l7, 0))
print(sum_pairs(l8, 10))