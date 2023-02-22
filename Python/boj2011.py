s = input()
n = len(s)

dp = [-1 for i in range(n)]

if s[n-1] == "0":
    dp[n-1] = 0
else:
    dp[n-1] = 1

if s[n-2] == "0":
    dp[n-2] = 0
elif "10" <= s[n-2:n] <= "26":
    dp[n-2] = dp[n-1] + 1
else:
    dp[n-2] = dp[n-1]

for i in range(n-3, -1, -1):
    if s[i] == "0":
        dp[i] = 0
    elif "10" <= s[i:i+2] <= "26":
        dp[i] = dp[i + 1] + dp[i + 2]
    else:
        dp[i] = dp[i+1]

    if dp[i] > 1000000:
        dp[i] %= 1000000
print(dp[0])
