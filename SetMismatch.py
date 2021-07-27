def findErrorNums(nums):

    nums = sorted(nums)
    presentSet = set(nums)
    actualSet = set([i for i in range(1, len(nums) + 1)])

    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            result = nums[i]

    diff = min(actualSet.difference(presentSet))
    return [result, diff]

print(findErrorNums([1,2,3,5,4,6,5]))

#[5, 7]