class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1 # 2
        tsum = 0
        
        # [0, 2, 7, 8, 11, 15]

        while first < last:
            tsum = numbers[first] + numbers[last]

            if tsum == target:
                return [first + 1, last + 1]
            if tsum <= target:
                first += 1
            else:
                last -= 1