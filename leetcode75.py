class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        # Method 1
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

        # Method 2
        l = []
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)
        for i in range(count0):
            l.append(0)
        for i in range(count1):
            l.append(1)
        for i in range(count2):
            l.append(2)
            
        return l


obj = Solution()
nums = [2, 0, 2, 1, 1, 1]
# nums = [2, 0, 1]
r = obj.sortColors(nums)
print(r)
