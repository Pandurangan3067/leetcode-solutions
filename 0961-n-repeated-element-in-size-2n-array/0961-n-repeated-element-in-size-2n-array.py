class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        a.sort()
        n=len(a)
        for i in range(n-1):
            if a[i]==a[i+1]:
                return a[i]
        return -1