M = 1000000
X = int(input())
dp = [1000000 for i in range(X+5)]
dp[1] = 0
dp[2] = 1
dp[3] = 1

i = 0
for i in range(4, X+1):
    if i == X+1:
        break
    a, b, c = M, M, M

    if i%3 == 0:
        a = dp[i//3] + 1

    if i%2 == 0:
        b = dp[i//2] + 1

    c = dp[i-1] + 1
    dp[i] = min(a, b, c)



print(dp[X])