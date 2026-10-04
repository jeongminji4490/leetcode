class Solution:
    def merge(self, low_arr: list[int], high_arr: list[int]) -> list[int]:
        l = h = 0
        sorted_arr = []

        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] <= high_arr[h]:
                sorted_arr.append(low_arr[l])
                l += 1
            else:
                sorted_arr.append(high_arr[h])
                h += 1
        while l < len(low_arr):
            sorted_arr.append(low_arr[l])
            l += 1
        while h < len(high_arr):
            sorted_arr.append(high_arr[h])
            h += 1

        return sorted_arr


    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        low_arr = nums[:mid]
        high_arr = nums[mid:]

        low_arr_ = self.sortArray(low_arr)
        high_arr_ = self.sortArray(high_arr)

        result = self.merge(low_arr_, high_arr_)

        return result
        