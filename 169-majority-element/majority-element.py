class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        n = len(nums)
        return nums[n // 2]
