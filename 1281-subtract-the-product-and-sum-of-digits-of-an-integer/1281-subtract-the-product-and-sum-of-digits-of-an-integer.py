class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            digit = n%10
            sum += digit
            product *= digit
            n //= 10
        return product - sum
        