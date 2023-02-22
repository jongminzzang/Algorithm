from collections import deque
import heapq

N, K = list(map(int, input().split()))
array = [(-1, False) for i in range(100001)]

h = []
heapq.heappush(h, (0, N))
array[N] = (0, True)


while array[K][0] == -1:
        # print(h)
        v = heapq.heappop(h)

        t = 2*v[1]
        while t < 100001 and t > 0:
            if array[t][1]:
                break
            elif array[t][0] == -1:
                array[t] = (v[0], True)
                heapq.heappush(h, (v[0], t))
            t = 2*t

        t = v[1]
        if t + 1 < 100001 and array[t+1][0] == -1:
            array[t+1] = (v[0]+1, False)
            heapq.heappush(h, (v[0]+1, t+1))
        if t-1 >= 0 and array[t-1][0] == -1:
            array[t-1] = (v[0]+1, False)
            heapq.heappush(h, (v[0]+1, t-1))


print(array[K][0])