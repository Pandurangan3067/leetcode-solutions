class Solution:
    def intersection(self, a: List[List[int]]) -> List[int]:
        d={}
        for i in a:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        l=[]
        n=len(a)
        for i,j in d.items():
            if j==n:
                l.append(i)
        l.sort()
        return l