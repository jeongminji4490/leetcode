class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 0
        sum = 0
        isFirst = True
        while n > 0:
            sum += n%10
            if product == 0 and isFirst == True:
                product = sum
                isFirst = False
            else:
                product *= n%10
            n //= 10
        return product - sum
        