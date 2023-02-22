import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
dp = []


t = l[0]
answer = l[0]
dp.append(l[0])

for i in range(1, n):
    if l[i] > dp[i-1] + l[i]:
        dp.append(l[i])
    else:
        dp.append(dp[i-1] + l[i])

    if dp[i] > answer:
        answer = dp[i]

print(answer)