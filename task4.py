def unique_in_order(iterable):
    return [string for index, string in enumerate(iterable) if index == 0 or iterable[index - 1] != string]


print(str(unique_in_order('AAAABBBCCDAABBB')))

