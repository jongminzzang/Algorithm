n = int(input())
l = list(map(int, input().split()))

dp = [0 for x in range(1001)]

for x in l:
    k = max(dp[0:x])
    dp[x] = k + 1
print(max(dp))
