class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {} 
        for k, n in enumerate(nums):
            diff = target - n
            if diff in mapp:
                return [mapp[diff], k]
            mapp[n] = k