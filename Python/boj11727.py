n = int(input())

dp = [0, 1, 3]
for x in range(3,n+1):
    k = dp[x-2]*2 + dp[x-1]
    dp.append(k % 10007)

# print(dp)
print(dp[n])