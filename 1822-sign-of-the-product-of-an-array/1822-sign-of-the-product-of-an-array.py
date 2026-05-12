class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sum = 1
        result = 0
        for num in nums:
            sum *= num
            if sum > 0:
                result = 1
            elif sum == 0:
                result = 0
            else:
                result = -1
        return result