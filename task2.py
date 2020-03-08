def disemvowel(string):
    symbols = 'qeuioa'
    symbols = symbols.upper() + symbols
    return ''.join([i for i in string if not i in symbols])


print(disemvowel('hello'))
print(disemvowel('Hello my sister Angelina'))
