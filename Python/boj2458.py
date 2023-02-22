import sys
input = sys.stdin.readline
N , M  = map(int, input().split())

m = [[502 for i in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    m[i][i] = 0

# m[i][j] : i 에서 j 까지 가는 비용
for i in range(M):
    i, j = map(int, input().split())
    m[i][j] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if m[i][j] != 502: pass
            elif m[i][k] + m[k][j] == 2:
                m[i][j] = 1

answer = 0
for i in range(1, N+1):
    b = True
    for j in range(1, N+1):
        if m[i][j] == 502 and m[j][i] == 502:
            b = False
            break
    if b:
        answer += 1

print(answer)
