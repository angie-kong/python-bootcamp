print('hello world')

#initializing, no need to specify type
name = "Angela"
age = 31
temperature = 25.54283094

#printing things
print(f"My name is {name}, and I am {age} years old. It is currently {temperature} degrees outside.")
print("My name is {}, and I am {} years old. It is currently {} degrees outside.".format(name, age, temperature))

#to print types - no primitive data types, only classes
print(type(name))
print(type(age))
print(type(temperature))

#features of f-string: can format things
print(f"{type(name) = }")

#a way around floats with f-strings
print(f"{temperature:.2f}") # .2f = 2 decimal points

#control flow

#if, else if, else statements
if age > 21:
    print("You are an adult") #four spaces
elif age == 21:
    print("Almost")
else:
    print("You're not an adult")

    #next time - functions and lists and dictionaries
