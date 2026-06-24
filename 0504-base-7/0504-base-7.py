class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
            
        is_negative = num < 0
        num = abs(num)
        result = []
        
        while num > 0:
            result.append(str(num % 7))
            num //= 7
            
        if is_negative:
            result.append("-")
            
        return "".join(reversed(result))