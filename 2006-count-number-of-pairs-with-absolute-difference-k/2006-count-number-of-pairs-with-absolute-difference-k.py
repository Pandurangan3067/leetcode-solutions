class Solution:
    def countKDifference(self, a: List[int], k: int) -> int:
        n=len(a)
        c=0
        if n==1:
            return 0
        else:
            for i in range(n-1):
                for j in range(i+1,n):
                    if abs(a[i]-a[j])==k:
                        c+=1
        return c