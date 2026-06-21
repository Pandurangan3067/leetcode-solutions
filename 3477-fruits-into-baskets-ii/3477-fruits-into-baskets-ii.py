class Solution:
    def numOfUnplacedFruits(self, f: List[int], b: List[int]) -> int:
        c,n=0,len(f)
        for i in range(n):
            for j in range(n):
                if f[i]<=b[j]:
                    f[i]=-1
                    b[j]=-1
                    break
            if f[i]!=-1:
                c+=1
            print(c)
        return c