



if __name__ == '__main__': #not required, nice thing to do
    #take user input

    # print("What is your name?")
    # name = input()
    # print(f"Hello, {name}")

    # bad, age gets returned as str
    # name1 = input("Enter yout name: ")
    # print(f"Hello {name1}")
    # age = input("Enter your age: ")
    #print(f"{type(age) = }")
    # print(f"You are {age} years old")

    age = int(input("Enter your age: "))
    years_left_to_live = 100 - age
    print(f"You have {years_left_to_live} years left to live")