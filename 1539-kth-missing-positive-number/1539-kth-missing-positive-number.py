class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        for i in range(1,max(a)+k+1):
            if i not in a:
                k-=1
                print(i,k)
            if k==0:
                return i 