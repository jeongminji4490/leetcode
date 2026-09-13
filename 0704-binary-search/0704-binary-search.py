class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        first = 0
        last = len(nums) - 1
        # mid = len(nums) // 2

        while first <= last:
            mid = (first + last) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

        return -1
            