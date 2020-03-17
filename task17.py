def same_structure_as(original, other):
    if type(original) != type([]) or type(other) != type([]):
        return False
    else:
        if len(original) != len(other):
            return False
    for i in range(len(original)):
        if type(original[i]) == type(1) or type(other[i]) == type(1):
            if type(original[i]) == type([]) or type(other[i]) == type([]):
                return False
        else:
            if len(original[i]) != len(other[i]):
                return False
            for j in range(len(original[i])):
                if type(original[i][j]) == type(1) or type(other[i][j]) == type(1):
                    if type(original[i][j]) == type([]) or type(other[i][j]) == type([]):
                        return False
                else:
                    if len(original[i][j]) != len(other[i][j]):
                        return False
    return True


print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[], [[], []]]))
print(same_structure_as([], {}))
print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
