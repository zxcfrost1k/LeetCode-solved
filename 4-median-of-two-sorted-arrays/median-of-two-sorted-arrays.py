class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mass = sorted(nums1 + nums2)
        long = len(mass)
        g = long // 2 - 1
        if len(mass) % 2 == 0:
            return (mass[g] + mass[g + 1]) / 2
        else:
            return mass[g + 1]