class Solution:
    def arithmeticTriplets(self, a: List[int], d: int) -> int:
        c=0
        n=len(a)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if abs(a[i]-a[j])==d and abs(a[j]-a[k])==d:
                        c+=1
        return c