class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        repetition = 0
        for item in arr:
            if item%2 == 1:
                repetition += 1
            else:
                repetition = 0
            if repetition == 3:
                return True
        
        return False
        