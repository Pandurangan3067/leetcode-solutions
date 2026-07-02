class Solution:
    def reversePrefix(self, s: str, ch: str) -> str:
        for i in range(len(s)):
            if s[i]==ch:
                return s[i::-1]+s[i+1:]
        return s
        