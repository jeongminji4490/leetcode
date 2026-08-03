class Solution:
    def reverse(self, x: int) -> int:
        formatted = f"{x}"
        reversed = formatted[::-1]
        result = 0
        is_negative = False

        left_range = -1*2**31
        right_range = 2**31-1

        if reversed[-1] == "-":
            is_negative = True
            reversed = reversed[:-1] + ""
            # result = 0 - int(reversed)
        if reversed[0] == "0":
            formatted = formatted.replace("0", '', 1)
            # result = int(reversed)
            

        if is_negative == True:
            result = 0 - int(reversed)
        else:
            result = int(reversed)
            
        if result < left_range or result > right_range:
            return 0
        else:
            return result
        
        
        