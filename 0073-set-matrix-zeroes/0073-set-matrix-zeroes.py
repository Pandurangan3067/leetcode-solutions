class Solution:
    def setZeroes(self, mi: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        m,n=len(mi),len(mi[0])
        for i in range(m):
            for j in range(n):
                if mi[i][j]==0:
                    l.append([i,j])
        for i in l:
            for j in range(n):
                mi[i[0]][j]=0
            for k in range(m):
                mi[k][i[1]]=0