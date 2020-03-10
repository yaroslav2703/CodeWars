def sum_pairs(ints, s):
    sum_list = []
    x = []
    for i in range(0, len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                x = [ints[i], ints[j]]
                sum_list = ints[i:j+1]
                for k in range(1, len(sum_list)-1):
                    for n in range(k + 1, len(sum_list)-1):
                        if sum_list[k] + sum_list[n] == s:
                            x = [sum_list[k], sum_list[n]]
                            sum_list = sum_list[k:n + 1]
                            return x
                else:
                    return x
    return None



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
