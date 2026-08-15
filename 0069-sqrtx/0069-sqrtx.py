class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        last = x

        while start <= last:
            mid = (start + last) // 2

            if (mid * mid) <= x: 
                start = mid + 1
            else: 
                last = mid - 1

        return last