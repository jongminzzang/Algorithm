import heapq
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    degree[u] += 1
    degree[v] += 1

h = []
for i in range(1, N+1):
    # (-indegree, n)
    heapq.heappush(h, (-degree[i], i))


answer = 0
while h:
    t = heapq.heappop(h)

    #갱신된 노드 였으면 pass
    if t[0] != -degree[t[1]]:

        pass

    elif degree[t[1]] == 0:
       break

    else:
        answer += 1
        degree[t[1]] = -1
        for x in graph[t[1]]:
            degree[x] -= 1
            heapq.heappush(h, (-degree[x], x))

print(answer)