class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        c=0
        n=len(a)
        for i in range(n-1):
            for j in range(i+1,n):
                if a[i]==a[j]:
                    c+=1
        return c