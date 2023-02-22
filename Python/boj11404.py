import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

m = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    m[i][i] = 0

# m[i][j] : i 에서 j 까지 가는 비용
for i in range(M):
    i, j, v= map(int, input().split())
    if m[i][j] > v:
        m[i][j] = v


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if m[i][j] > m[i][k] + m[k][j]:
                m[i][j] = m[i][k] + m[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if m[i][j] == INF:
            print(0, end=" ")
        else:
            print(m[i][j], end=" ")
    print()
