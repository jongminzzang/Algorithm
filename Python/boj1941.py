from itertools import combinations
from collections import deque

m = []
t = [(i, j) for i in range(5) for j in range(5)]

for i in range(5):
    m.append(list(input()))


def most_s(p_list):
    global m
    cnt = 0
    for p in p_list:
        if m[p[0]][p[1]] == 'S':
            cnt += 1

    if cnt > 3:
        return True
    else:
        return False


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def ad(p_list):
    d = deque()
    d.append(p_list[0])
    v = [p_list[0]]
    while d:
        k = d.pop()
        kx = k[0]
        ky = k[1]
        for i in range(4):
            if (kx + dx[i], ky + dy[i]) in p_list and (kx + dx[i], ky + dy[i]) not in v:
                v.append((kx + dx[i], ky + dy[i]))
                d.append((kx + dx[i], ky + dy[i]))
    if len(v) == 7:
        return True
    else:
        return False


ans = 0
combi = combinations(t, 7)
for i, x in enumerate(combi):
    if most_s(x):
        if ad(x):
            ans += 1

print(ans)
