"""Write a python program to check whether
the sum of two numbers of a list is equals to the a target value or not?"""


def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        value = target - nums[i]
        if value in dic:
            return [dic[value], i]
        dic[nums[i]] = i
    return []


nums = [2, 7, 13, 21]
target = 9
call = twosum(nums, target)
m, n = call
print(f"The Numbers are {nums[m]} and {nums[n]}")
