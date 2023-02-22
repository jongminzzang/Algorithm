import sys
input = sys.stdin.readline

l = input()
N = len(l)
dp = [[0 for j in range(N+1)] for i in range(N+1)]

# dp 테이블 채우기
# [start, end)
for i in range(N):
    dp[i][i+1] = 1

for i in range(N-1):
    if l[i] == l[i+1]:
        dp[i][i+2] = 1

# [ j, j + i )
for i in range(3, N+1):
    for j in range(0, N):
        if j + i > N:
            break
        else:
            if l[j] == l[j+i-1]:
                dp[j][j+i] = dp[j+1][j+i-1]


answer = [N for i in range(N+1)]
answer[0] = 0
answer[1] = 0
answer[2] = 1
answer[3] = 1 + (l[0]!=l[1])

for x in range(3,N+1):
    for k in range(0, x):
        if dp[k][x]:
            answer[x] = min(answer[x], answer[k]+1)

print(answer)