class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        e,o=[],[]
        for i in range(len(a)):
            if a[i]%2==0:
                e.append(a[i])
            else:
                o.append(a[i])
        return e+o