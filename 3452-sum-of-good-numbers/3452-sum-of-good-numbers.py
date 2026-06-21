class Solution:
    def sumOfGoodNumbers(self, a: List[int], k: int) -> int:
        n=len(a)
        s=0
        for i in range(n):
            if i-k>=0 and i+k<n:
                if a[i-k]<a[i] and a[i+k]<a[i]:
                    s+=a[i]
            elif i-k>=0 and a[i-k]<a[i]:
                s+=a[i]
            elif i+k<n and a[i+k]<a[i]:
                s+=a[i]
        return s
                