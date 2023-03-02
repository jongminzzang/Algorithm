import heapq

N = int(input())

t = [0 for i in range(N)]
m = [[] for i in range(N)]

cnt = [0 for i in range(N)]


h = []

for i in range(N):
    l = list(map(int, input().split()))
    t[i] = l[0]
    if len(l) == 2:
        heapq.heappush(h, (t[i], i))
    else:
        for x in l[1:-1]:
            m[x-1].append(i)
            cnt[i] += 1

ans = [0 for i in range(N)]


while h:
    k = heapq.heappop(h)
    ans[k[1]] = k[0]

    for x in m[k[1]]:
        cnt[x] -= 1
        if cnt[x] == 0:
            heapq.heappush(h, (k[0]+t[x], x))

for a in ans:
    print(a)