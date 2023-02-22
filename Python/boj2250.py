N = int(input())
graph = [[] for i in range(N+1)]
root = -1
find_root = [True for i in range(N+1)]

for i in range(N):
    h, l, r = map(int, input().split())
    graph[h] = [l, r]
    if l != -1:
        find_root[l] = False
    if r != -1:
        find_root[r] =False

for i, x in enumerate(find_root[1:]):
    if x:
        root = i+1
        break

depth = 1
x = 0
t = root

def inorder(t, depth):
    global graph, level, x
    # 왼쪽 순회
    if graph[t][0]  != -1:
        inorder(graph[t][0], depth + 1)

    x += 1
    graph[t].append(x)
    graph[t].append(depth)

    # 오른쪽 순회
    if graph[t][1]  != -1:
        inorder(graph[t][1], depth+1)

level =[[] for i in range(N+1)]

inorder(t, depth)
for x in graph[1:]:
    level[x[3]].append(x[2])



g_max = -1
g_index = -1
for i, x in enumerate(level):
    if not x :
        continue
    M = max(x)
    m = min(x)
    if M-m+1 > g_max:
        g_max = M-m+1
        g_index = i

print(g_index, g_max)
