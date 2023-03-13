N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
le = len(A)
b = [False for i in range(le)]


# list l,
def dfs(t, d):
    global A, K, ans, b
    if d == le:
        if t >= 0:
            ans += 1

    else:
        for i in range(le):
            if not b[i]:
                k = t + A[i] - K
                if k >= 0:
                    b[i] = True
                    dfs(k, d + 1)
                    b[i] = False


dfs(0, 0)
print(ans)