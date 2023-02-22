import sys
import heapq
# sys.stdin = open('t.txt', 'r')

input = sys.stdin.readline

M, N = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]
dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] =1


# 높이, x, y
h = []
heapq.heappush(h, (-l[0][0], 0, 0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while h:
    hi, tx, ty = heapq.heappop(h)
    for i in range(4):
        ix = tx + dx[i]
        iy = ty + dy[i]
        if 0 <= ix < M and 0 <= iy < N and l[ix][iy] < -hi:
            if dp[ix][iy] == 0:
                heapq.heappush(h, (-l[ix][iy], ix, iy))
            dp[ix][iy] += dp[tx][ty]
print(dp[M-1][N-1])