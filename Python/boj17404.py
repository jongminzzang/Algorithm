import sys
input = sys.stdin.readline
N = int(input())

rgb = [list(map(int, input().split())) for i in range(N)]
dp = [[0,0,0] for i in range(N)]

answer = 10000000
# R 시작
dp[1][0] = 10000000
dp[1][1] = rgb[0][0] + rgb[1][1]
dp[1][2] = rgb[0][0] + rgb[1][2]
for i in range(2, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
answer = min(answer, dp[N-1][1], dp[N-1][2])

# G 시작
dp[1][1] = 10000000
dp[1][0] = rgb[0][1] + rgb[1][0]
dp[1][2] = rgb[0][1] + rgb[1][2]
for i in range(2, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
answer = min(answer, dp[N-1][0], dp[N-1][2])


# 초록집 시작
dp[1][2] = 10000000
dp[1][0] = rgb[0][2] + rgb[1][0]
dp[1][1] = rgb[0][2] + rgb[1][1]
for i in range(2, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
answer = min(answer, dp[N-1][0], dp[N-1][1])


print(answer)