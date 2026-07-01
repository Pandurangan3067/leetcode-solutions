class Solution:
    def greatestLetter(self, s: str) -> str:
        ans=""
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in s and ch.upper() in s:
                ans=ch
        return ans.upper()