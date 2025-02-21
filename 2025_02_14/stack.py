

if __name__ == '__main__':
    # default lists are good for stack operation because you can use append and pop (from the end)
    # stack = LIFO
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack)

    #.pop() remoes and returns the last element
    # you can use it to just remove, but also to get value

    stack.pop()
    print(stack)

    last_val = stack.pop()
    print(last_val)
    print(stack)

    stack.pop()
    print(stack)

    # pop fro empty list error
    stack.pop()