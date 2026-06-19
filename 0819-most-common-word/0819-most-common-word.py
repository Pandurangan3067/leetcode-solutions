import re
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        s = re.sub(r"[!?',;.]", " ", p)
        s=s.lower().split()
        d={}
        for w in s:
            if w not in d:
                d[w]=1
            else:
                d[w]+=1
        d = dict(sorted(d.items(), key=lambda x: x[1],reverse=True))
        for i,j in d.items():
            if i in banned:
                continue
            else:
                return i