


if __name__ == '__main__':
    # dictionaries are hashmaps
    # constant time adding and lookup

    # no need to specify types with keys and values (unlike Java / C++)
    # does not enforce type, will just keep accepting
    # good - convenient, bad - lead to bugs

    #empty dictionary
    empty_dict = {}
    # {} = empty dictionary
    # [] = empty list
    empty_dict = dict() # can also define with keyword

    # to add key value pairs: use []
    empty_dict["name"] = "Alison"
    print(empty_dict) # built in toString method - will print whole dict without loops

    # to get value, use same []
    print(empty_dict["name"])

    # define with existing key-value pairs
    students_dict = {
        123: "Alison",
        456: "Brian",
        789: "Carol",
    }
    print(students_dict)

    # access specific from dict - will print name at that value
    print(students_dict[123])

    # access key that DNE - KeyError
    # print(students_dict[567])

    # to avoid key errors, use .get() method or check if key exists
    print(students_dict.get(567))
    # returns None

    # or

    if 567 in students_dict: # will only check keys, not values
        print(students_dict[567])
    else: 
        print("Key not here")

    # how to handle all keys and all values:

    # there is a .keys() method - don't care about student names, care about ID's aka keys
    print(students_dict.keys())
    # dict_keys special object

    # there is also a .values() method
    print(students_dict.values())
    # dict_values