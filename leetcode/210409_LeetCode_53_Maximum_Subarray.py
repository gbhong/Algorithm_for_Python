class Solution:
    def maxSubArray(self, nums: list):
        curr = nums[0];res = [curr]

        for i in range(1, len(nums)):
            if curr >= 0:
                if nums[i] < 0:
                    res.append(curr)
                curr += nums[i]
            else:
                if nums[i] < 0:
                    res.append(curr)
                curr = nums[i]

        res.append(curr)

        return max(res)