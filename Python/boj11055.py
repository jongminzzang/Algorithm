import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(1001)]

for x in l:
    if dp[x] < max(dp[:x])+x:
        dp[x] = max(dp[:x])+x
print(max(dp))