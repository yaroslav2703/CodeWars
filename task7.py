def stray(arr):
    all_numbers = set(arr)
    return [i for i in all_numbers if arr.count(i) == 1][0]


print(stray([1, 1, 1, 1, 1, 1, 2]))
print(stray([2, 3, 2, 2, 2]))
print(stray([3, 2, 2, 2, 2]))