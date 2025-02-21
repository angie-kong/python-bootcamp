

def reverse_vowels(s: str) -> str:
    letters = list(s)
    vowels = []
    result = []

    for letter in letters:
        if letter.lower() in "aeiou":
            vowels.append(letter)
    
    for letter in letters:
        if letter.lower() in "aeious":
            result.append(vowels.pop())
        else:
            result.append(letter)
    
    return "".join(result)

if __name__ == '__main__':
    s = "IceCreAm"
    print(reverse_vowels(s))

    
    # reverse vowels into new variable/list
    # vowels = reversed(vowels)

    # returns nothing
    # vowels.reverse()
    
    # vowels = vowels[::-1]
    