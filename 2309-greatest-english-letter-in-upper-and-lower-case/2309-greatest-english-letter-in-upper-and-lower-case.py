class Solution:
    def greatestLetter(self, s: str) -> str:
        c=0
        for i in range(len(s)-1):
            if s[i].isupper() and s[i].lower() in s[i+1:]:

                if c<ord(s[i]):
                    c=ord(s[i])
            elif s[i].islower() and s[i].upper() in s[i+1:]:
            
                if c<ord(s[i])-32:
                    c=ord(s[i])-32
          
        return chr(c) if c!=0 else ""