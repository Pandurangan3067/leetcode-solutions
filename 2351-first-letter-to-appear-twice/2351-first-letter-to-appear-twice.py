class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=set()
        for i in s:
            if i in l:
                return i
            else:
                l.add(i)
