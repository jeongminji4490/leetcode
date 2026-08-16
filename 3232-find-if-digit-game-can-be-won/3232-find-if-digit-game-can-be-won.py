class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1 = 0
        sum2 = 0

        for i in nums:
            if i < 10:
                sum1 += i
            else:
                sum2 += i

        return True if (sum1 > sum2) or (sum2 > sum1) else False