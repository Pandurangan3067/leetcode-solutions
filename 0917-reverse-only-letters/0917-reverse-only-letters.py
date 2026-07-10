class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        while l<=r:
            if s[l].isalpha() and s[r].isalpha():
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
                continue
            elif s[l].isalpha():
                r-=1
                continue
            elif s[r].isalpha():
                l+=1
                continue
            else:
                r-=1
                l+=1
        return "".join(s)