class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqaures_list = []
        
        for n in nums:
            sqaures_list.append(n*n)

        sqaures_list.sort()
        return sqaures_list

        