import heapq

N, K = map(int, input().split())

j = []
for i in range(N):
    j.append(list(map(int, input().split())))

c = []
for i in range(K):
    c.append(int(input()))

# 보석의 무게 기준으로 정렬, 가방의 담을 수 있는 무게 기준으로 정렬
j.sort()
c.sort()

# 현재 가방의 무게 보다는 작은 상태에서 가치 기준으로 생성한 힙을 유지
value_heap = []

ans = 0
idx = 0
# i 번째 가방의 무게 x
for i, x in enumerate(c):
    # 가방 하나를 추가
    while True:
        if idx >= len(j):
            break
        if j[idx][0] <= x:
            heapq.heappush(value_heap, (-j[idx][1], j[idx][0]))
            idx += 1
        else:
            break

    # 가방에 넣을 수 있는 최대 가치의 보석
    if value_heap:
        ans -= heapq.heappop(value_heap)[0]


print(ans)