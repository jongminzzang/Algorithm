from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        d = deque()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        len_i = len(mat)
        len_j = len(mat[0])
        
        check = [[False for _ in range(len_j)] for _ in range(len_i)]
        
        
        for i in range(len_i):
            for j in range(len_j):
                if mat[i][j] == 0:
                    check[i][j] = True
                    d.append((i,j,0))
        
        while d:
            i, j, x = d.popleft()
            for k in range(4):
                tx = i+dx[k]
                ty = j+dy[k]
                if -1 < i+dx[k] and i+dx[k] < len_i and -1 < j+dy[k] and j+dy[k] < len_j:
                    if check[tx][ty] == True:
                        pass
                    else:
                        mat[tx][ty] = x+1
                        check[tx][ty] = True
                        d.append((tx,ty,x+1))
    
        return mat
