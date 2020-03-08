def valid_parentheses(string):
    stack = []
    for c in string:
        if c is '(':
            stack.append('(')
        if c is ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
