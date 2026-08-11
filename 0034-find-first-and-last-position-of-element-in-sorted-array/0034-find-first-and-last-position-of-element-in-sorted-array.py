class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return [-1, -1]

        result = []
        first = 0
        last = len(nums) - 1

        left = -1

        while first <= last:
            mid = (first + last) // 2

            if target == nums[mid]:
                left = mid
                last = mid - 1
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

        first = 0
        last = len(nums) - 1

        right = -1

        while first <= last:
            mid = (first + last) // 2

            if target == nums[mid]:
                right = mid
                first = mid + 1
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

        
        return [left, right]
                

        





        