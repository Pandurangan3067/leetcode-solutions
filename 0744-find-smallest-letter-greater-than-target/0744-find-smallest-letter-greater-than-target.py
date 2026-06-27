from typing import List

class Solution:
    def nextGreatestLetter(self, s: List[str], t: str) -> str:
        l, f = 0, len(s) - 1
        
        while l <= f:
            m = (l + f) // 2
            

            if s[m] <= t:
                l = m + 1

            else:
                f = m - 1
                
        if l == len(s):
            return s[0]
            
        return s[l]