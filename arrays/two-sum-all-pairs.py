def twoSum(nums, target):
    ht = {}
    pairs = []

    for i in range(len(nums)):
        currentSum = target - nums[i]

        if nums[i] in ht:
            pairs.append([ ht[nums[i]], nums[i] ])
        
        else:
            ht[currentSum] = nums[i]

    return pairs

print(twoSum([2,7,7], 9))
