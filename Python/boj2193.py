dp = [0, 1, 1, 2]

n = int(input())

for x in range(4, n+1):
    dp.append(dp[x-1]+dp[x-2])

print(dp[n])