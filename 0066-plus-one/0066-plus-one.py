class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        str_digit = ""
        for digit in digits:
            str_digit = str_digit + str(digit)

        str_digit_list = list(str(int(str_digit) + 1))

        for str_digit in str_digit_list:
            result.append(int(str_digit))

        return result
