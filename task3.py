def namelist(names):
    string = ''
    i = 0
    while i < len(names)-1:
        if len(string) == 0:
            string = names[i]['name']
            i = i + 1
        else:
            string = string + ', ' + names[i]['name']
            i = i + 1
    else:
        if len(string) == 0:
            if len(names) == 1:
                string = names[len(names) - 1]['name']
            else:
                string = ''
        else:
            string = string + ' & ' + names[len(names)-1]['name']
    return string


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))
