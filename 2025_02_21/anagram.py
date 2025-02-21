

def isAnagram(s, t) -> bool:
    letters = {}
    for c in s:
        if c in letters: # store and increment letter frequencies in s
            letters[c] += 1
        else:
            letters[c] = 1
    print(letters)
    
    for c in t: # decrement frequencies as you encounter them in t
        if c in letters:
            letters[c] -= 1
            if letters[c] == 0:
                del letters[c]
        else:
            return False
    
    if len(letters) == 0:
        return True
    return False

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))