def twoSum(nums,target):
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                if i not in output and j not in output:
                    output = [i,j]
    return output

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
