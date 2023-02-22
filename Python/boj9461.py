N = int(input())
answer = [int(input()) for _ in range(N)]

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(9, max(answer)):
    dp.append(dp[i]+dp[i-4])

for x in answer:
    print(dp[x-1])