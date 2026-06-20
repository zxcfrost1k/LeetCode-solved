class Solution:
    def searchInsert(self, nums, target) -> int:
     try:
          return nums.index(target)
     except:
          if target < nums[0]:
               return 0

          elif target > nums[-1]:
               return len(nums)

          i = 0
          while nums[i] < nums[-1]:
               if nums[i] > target:
                    return i
               i += 1
          return i