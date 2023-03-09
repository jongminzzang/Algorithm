from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
l = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

d = deque()

visit[1] = -1
d.append(1)

while d:
    t = d.popleft()
    # print(t)
    for x in l[t]:
        if visit[x] == 0:
            visit[x] = t
            d.append(x)


for x in visit[2:]:
    print("%d\n" %x)