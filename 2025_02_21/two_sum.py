
# to add to hash map
# dict[key] <= value

# enumerate - tuple with 2 elements: index and value at index




def twoSum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        hashmap[n] = i
    print(hashmap)
    for i, n in enumerate(nums):
        complement = target - n
        if complement in hashmap:
            comp_index = hashmap[complement]
            return [i, comp_index]


if __name__ == '__main__':
    test1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(test1, target1))