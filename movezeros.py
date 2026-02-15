class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        i = 0
        for j in range(l):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
