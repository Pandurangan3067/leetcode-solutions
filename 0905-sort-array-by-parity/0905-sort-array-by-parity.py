class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        li=[]
        for i in range(len(a)):
            if a[i]%2==0:
                li.insert(0,a[i])
            else:
                li.append(a[i])
        return li