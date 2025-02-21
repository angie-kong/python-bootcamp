

if __name__ == '__main__':
    # no arrays in Python, only lists
    #contiguous array, but also has variable length - similar to ArrayLists in Java, or vector in C++

    # string list
    names = ["Alice", "Bob", "Carol", "Dennis", "Evelyn"]

    # int list
    ages = [25, 78, 45, 68, 22]

    # mixed type list
    mixed = ["Alice", 25, "Bob", 78, "Carol", 45, "Dennis", 68, "Evelyn", 22]

    # nested lists
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # iterating through lists
    # simple index based for loop
    for i in range(len(names)):
        print(names[i])
    
    # range function returns an iterable object
    # range(3) = range(0, 3), parameter is outer bound starting from 0
    # range is exclusive

    # skipping every other element
    # starting, ending, skip by
    for i in range(0, len(names), 2):
        print(f"{i = }; {names[i] = }")

    # for each loop - only gives element at index, not the index
    # more convenient, no need for range and length and stuff
    for name in names:
        print(name)
    
    # enumerate is convenient when you need both index and value at index
    for i, name in enumerate(names):
        print(f"{i = }; {name = }")
    
    print("Let's do a class roster.")
    
    # class_roster_A = []
    # name = input("Enter student's name: ")
    # while name != "":
    #     # append adds to end of list - convenient, cheap
    #     class_roster_A.append(name)
    #     name = input("Enter student's name: ")
    # print(class_roster_A)

    class_roster_B = []
    while True:
        name = input("Enter student name: ")
        if name == "":
            break
        class_roster_B.append(name)
    print(class_roster_B)

    