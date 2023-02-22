from collections import deque
import sys
input = sys.stdin.readline


i = 1
while True:

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    node = [[] for _ in range(n+1)]
    tree = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    # print(node)
    # union find?
    u = 1
    cycle_set = set()
    for k in range(1, n+1):
        # 이미 어떤 그레프에 속하는지 확인이 된 경우
        if tree[k] != 0:
            pass
        # 그게 아닌 경우
        else:
            tree[k] = u
            d = deque()
            for x in node[k]:
                tree[x] = u
                d.append((k, x))
            cycle = False

            while d:
                before, now = d.popleft()

                for x in node[now]:
                    # 전 노드에서 바로 뒤로는 가지 않도록
                    if x == before:
                        continue
                    # 이미 들린 노드 -> cycle 존재함
                    # 큐에 다시 집어 넣을 필요 없음
                    elif tree[x] != 0:
                        cycle = True
                    else:
                        tree[x] = u
                        d.append((now, x))
            if cycle:
                cycle_set.add(u)
            u += 1
        # print(k, tree)
    # print()
    T = u - len(cycle_set) -1
    s = ""
    if T == 0:
        s = "No trees."
    elif T == 1:
        s = "There is one tree."
    else:
        s = f"A forest of {T} trees."
    print(f"Case {i}: {s}")
    i += 1