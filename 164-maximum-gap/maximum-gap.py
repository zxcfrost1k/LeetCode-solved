class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums) - 1):
            res.append(nums[i + 1] - nums[i])
        
        return max(res)