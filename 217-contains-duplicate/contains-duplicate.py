class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        new_nums = set(nums)
        if len(new_nums) == len(nums):
            return False
        else:
            return True
        