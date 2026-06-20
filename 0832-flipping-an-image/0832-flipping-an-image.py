class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        for i in range(len(a)):
            a[i].reverse()
            for  j in range(len(a[i])):
                if a[i][j]==0:
                    a[i][j]=1
                else:
                    a[i][j]=0
        return a