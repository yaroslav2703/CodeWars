def duplicate_encode(word):
    final = ''
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            final = final + ')'
        else:
            final = final + '('
    return final


print(duplicate_encode('din'))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))