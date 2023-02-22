n, k = list(map(int, input().split()))

p = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for x in p:
    for i in range(x,k+1):
        dp[i] += dp[i-x]

print(dp[-1])
