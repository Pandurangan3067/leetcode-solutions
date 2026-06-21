class Solution:
    def transformArray(self, a: List[int]) -> List[int]:
        e,o=0,0
        for i in range(len(a)):
            if a[i]%2==0:
                e+=1
            else:
                o+=1
        return [0]*e+[1]*o