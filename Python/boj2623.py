from collections import deque

d = deque()
N, M = map(int, input().split())

k = [i for i in range(1,N+1)]
l = {i : set() for i in range(N+1)}
out = {i : set() for i in range(N+1)}



for _ in range(M):
    t = list(map(int, input().split()))
    x, seq = t[0], t[1:]

    for i in range(x):
        now = seq[i]
        for j in range(i+1, x):
                    l[now].add(seq[j])

    seq = seq[::-1]
    for i in range(x):
        now = seq[i]
        for j in range(i+1, x):
                    out[now].add(seq[j])

v = []
for x in range(0, N+1):
    v.append(len(out[x]))
    if not out[x] and x != 0:
        d.append(x)


answer = []
while d:
    t = d.popleft()
    answer.append(t)
    for x in l[t]:
        v[x] -= 1
        if v[x] == 0:
            d.append(x)

if len(answer) == N:
    for x in answer:
        print(x)
else:
    print(0)