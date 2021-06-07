class Solution:
    def containsDuplicate(self, nums: list):
        return abs((len(set(nums)) == len(nums))-1)