def sum_of_intervals(intervals):
    a = ()
    for j in intervals:
        a = a + tuple(range(j[0], j[1]))
    a = sorted(list(set(a)))
    return len(a)

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
