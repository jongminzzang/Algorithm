from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        len_i = len(grid)
        len_j = len(grid[0])
        
        d = deque()
        fresh = []
        
        for i in range(len_i):
            for j in range(len_j):
                if grid[i][j] == 2:
                    d.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
                    
        max_day = 0
        while d:
            x, y, day = d.popleft()
            for k in range(4):
                tx = x + dx[k]
                ty = y + dy[k]
                if -1 < tx and tx < len_i and -1 < ty and ty < len_j:
                    if grid[tx][ty] == 1:
                        grid[tx][ty] = 2
                        d.append((tx, ty, day+1))
                        max_day = day+1
        
        for x,y in fresh:
            if grid[x][y] == 1:
                max_day = -1
                break
        
        return max_day
