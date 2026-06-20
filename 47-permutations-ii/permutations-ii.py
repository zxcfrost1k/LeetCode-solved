class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(y) for y in set([x for x in permutations(nums)])]
