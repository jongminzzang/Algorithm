N = int(input())
p = list(map(int, input().split()))
p = [0] + p

dp = [0 for x in range(N+1)]

for k in range(1,N+1):
    t = []
    
    for x in range(0, k):
        t.append((dp[x] + p[k-x]))
    dp[k] = max(t)

print(dp[-1])
