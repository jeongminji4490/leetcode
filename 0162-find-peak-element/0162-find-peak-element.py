class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_idx = 0

        first = 0
        last = (len(nums) - 1) // 2

        while first <= last:
            if nums[last] > nums[max_idx]:
                max_idx = last
                # last = last - 1

            # first += 1
            last = last - 1

        if len(nums) % 2 != 0:
            first = (len(nums) + 1) // 2
        else:
            first = len(nums) // 2 # 2

        last = len(nums) - 1 # 3

        while first <= last:
            # if nums[2] > nums[1] -> 3 > 2
            if nums[first] > nums[max_idx]:
                max_idx = first # 2
                # first = first + 1 # 3

            # last -= 1 2
            first = first + 1

        return max_idx
            
            

        