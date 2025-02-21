
def valid_parentheses_v2(s):
    lookup = { # creating dictionary
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for c in s:
        if c in lookup.values():
            stack.append(c)
        else:
            # know for sure here that c is closing
            if len(stack) == 0:
                return False
            expected = lookup[c]
            if stack.pop() != expected:
                return False
    
    return len(stack) == 0
# equivalent to: 
# if len(stack) == 0:
#         return True
#     return False


# define function
def valid_parentheses(s): 
    stack = []
    for c in s:
        # print(c, end="") # no new line
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if len(stack) != 0:
                top_of_stack = stack[-1]
            else:
                return False
            if c == ')' and top_of_stack == '(':
                stack.pop()
            elif c == '}' and top_of_stack == '{':
                stack.pop()
            elif c == ']' and top_of_stack == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False

if __name__ == '__main__':
    test1 = "()"
    test2 = "()[]{}"
    test3 = "(]"
    test4 = "([])"

    # print(valid_parentheses(test1)) # True
    # print(valid_parentheses(test2)) # True
    # print(valid_parentheses(test3)) # False
    # print(valid_parentheses(test4)) # True

    print(valid_parentheses_v2(test1)) # True
    print(valid_parentheses_v2(test2)) # True
    print(valid_parentheses_v2(test3)) # False
    print(valid_parentheses_v2(test4)) # True


