class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for e in accounts:
            if sum(e) > result:
                result = sum(e)

        return result
        