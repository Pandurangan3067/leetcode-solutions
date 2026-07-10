class Solution:
    def reverseVowels(self, s: str) -> str:
        i="aeiouAEIOU"
        l,r=0,len(s)-1
        s=list(s)
        while l<=r:
            if s[l] in i and s[r] in i:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] in i and s[r] not in i:
                r-=1
            elif s[r] in i and s[l] not in i:
                l+=1
            else:
                l+=1
                r-=1
        return "".join(s)
