# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # n = 5 (1, 2, 3, 4, 5)
        first = 1
        last = n
        result = 0

        while first <= last:
            mid = (first + last) // 2

            if isBadVersion(mid):
                result = mid
                last = mid - 1
            else:
                first = mid + 1

        return result

        