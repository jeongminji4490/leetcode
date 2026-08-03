class Solution:
    def reverse(self, x: int) -> int:
        reversed = f"{x}"[::-1]

        left_range = -1*2**31
        right_range = 2**31-1

        if reversed[-1] == "-":
            reversed = "-" + reversed[:-1]
        if reversed[0] == "0" and len(reversed) != 1:
            reversed = reversed.replace("0", '', 1)
            
        if int(reversed) < left_range or int(reversed) > right_range:
            return 0
        else:
            return int(reversed)
        
        
        