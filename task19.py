def persistence(n):
    my_list = list(str(n))
    my_count = 0
    while len(my_list) > 1:
        comp = 1
        for i in my_list:
            comp = comp * int(i)
        my_list = list(str(comp))
        my_count += 1
    return my_count


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))




