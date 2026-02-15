def maxProduct(nums):
    min_val = max_val = ans = nums[0]

    for i in range(1, len(nums)):
        d = nums[i]

        # Store previous values before updating
        prev_max = max_val
        prev_min = min_val

        max_val = max(d, prev_max * d, prev_min * d)
        min_val = min(d, prev_max * d, prev_min * d)

        ans = max(ans, max_val)

    return ans
nums = [2, 3, -2, 4]
r = maxProduct(nums)
print(r)
