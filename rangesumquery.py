class NumArray(object):

    def __init__(self, nums):
        self.num = nums

    def sumRange(self, left, right):
        sum = 0
        while left <= right:
            sum += self.num[left]
            left += 1
        return sum
