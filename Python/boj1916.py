import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
h = []

for _ in range(M):
    s, e, v = list(map(int, input().split()))
    graph[s].append([v, e])


S, E = list(map(int, input().split()))
des = [-1 for i in range(N+1)]
des[S] = 0
for x in graph[S]:
    heapq.heappush(h, x)

while des[E] == -1:
    v, e = heapq.heappop(h)
    if des[e] != -1:
        pass
    else:
        des[e] = v
        for x in graph[e]:
            tv = v + x[0]
            heapq.heappush(h, [tv, x[1]])
    # print(des)


print(des[E])