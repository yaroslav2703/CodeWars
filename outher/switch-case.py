def a(header):
    print(header)


def b(header):
    print(header)


def c(header):
    print(header)


fc = { 0: {0: a, 1: b, 2: c},
       1: {0: b, 1: c, 3: a}}


def createTable(headers, q,  hid):
    f = fc[q][hid]
    f(headers[hid])


createTable([1, 2, 3], 0, 0)