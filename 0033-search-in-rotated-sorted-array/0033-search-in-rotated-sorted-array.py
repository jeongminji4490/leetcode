class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2

            if target == nums[mid]:
                return mid
            
            if nums[first] <= nums[mid]:
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] < target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1

        return -1