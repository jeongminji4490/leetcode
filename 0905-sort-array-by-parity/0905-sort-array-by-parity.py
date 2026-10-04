class Solution:
    def quick_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        low_arr = []
        high_arr = []

        for e in arr[1:]:
            if e < pivot:
                low_arr.append(e)
            else:
                high_arr.append(e)

        return self.quick_sort(low_arr) + [pivot] + self.quick_sort(high_arr)


    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums

        # pivot = nums[0]
        even_arr = []
        odd_arr = []

        sorted_arr = []

        for num in nums:
            if num % 2 == 0:
                even_arr.append(num)
            else:
                odd_arr.append(num)

        if even_arr:
            even_arr = self.quick_sort(even_arr)

        if odd_arr:
            odd_arr = self.quick_sort(odd_arr)

        result = []

        for n in even_arr:
            result.append(n)
        
        for n in odd_arr:
            result.append(n)

        return result

        


        
        
        