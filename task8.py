import string


def is_pangram(s):
    for i in string.ascii_lowercase:
        if s.lower().count(i) == 0:
            return False

    else:
        return True

print(is_pangram('abcdefghijklmopqrstuvwxyz'))

