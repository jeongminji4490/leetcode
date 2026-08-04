class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0

        min_val = min(nums)
        max_val = max(nums)

        if target < min_val:
            return 0
        if target > max_val:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] > target:
                result = i
                break
            if nums[i] == target:
                result = i
                break
        
        return result