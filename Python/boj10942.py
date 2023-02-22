import sys
print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
l = input().split()
dp = [['0' for j in range(N+1)] for i in range(N+1)]

# dp 테이블 채우기
# [start, end)
for i in range(N):
    dp[i][i+1] = '1'

for i in range(N-1):
    if l[i] == l[i+1]:
        dp[i][i+2] = '1'

# [ j, j + i )
for i in range(3, N+1):
    for j in range(0, N):
        if j + i > N:
            break
        else:
            if l[j] == l[j+i-1]:
                dp[j][j+i] = dp[j+1][j+i-1]

answer = []
M = int(input())
for x in range(M):
    start, end = map(int,input().split())
    answer.append(dp[start-1][end])

for x in answer:
    print(x+'\n')