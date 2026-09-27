class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0] or target < nums[0]:
                return 0
            else:
                return 1

        first = 0
        last = len(nums) - 1
        
        while first <= last:
            mid = (first + last) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        
        return first
        