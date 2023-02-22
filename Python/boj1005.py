import heapq
import sys
input = sys.stdin.readline

T = int(input())

answer = []

for _ in range(T):
    # N: 건물의 개수, K: 건설 순서 규칙
    N, K = map(int, input().split())

    time = [0] + list(map(int, input().split()))
    graph = [[] for i in range(N+1)]
    in_degree =[0 for i in range(N+1)]
    h = []

    for _ in range(K):
        # X를 지어야 Y를 지을 수 있음
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    des = int(input())


    for i in range(1, N+1):
        if in_degree[i] == 0:
            # 완성되는 시간, 건물번호
            heapq.heappush(h, (time[i], i))
    now_t = 0
    while h:
        t = heapq.heappop(h)
        now_t = t[0]
        if t[1] == des:
            break
        # compelete.add(t[1])

        for v in graph[t[1]]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(h, (now_t+time[v], v))
    answer.append(now_t)

for a in answer:
    print(a)