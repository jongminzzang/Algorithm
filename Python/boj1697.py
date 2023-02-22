from collections import deque

N, K = list(map(int, input().split()))
array = [-1 for i in range(100001)]

d = deque()
array[N] = 0
d.append(N)

while array[K] == -1:
    t = d.popleft()

    if t + 1 > 100000:
        pass
    elif array[t+1] == -1:
        array[t+1] = array[t] + 1
        d.append(t+1)

    if t-1 < 0:
        pass
    elif array[t-1] == -1:
        array[t-1] = array[t] + 1
        d.append(t-1)

    if t*2 > 100000:
        pass
    elif array[t*2] == -1:
        array[t*2] = array[t] + 1
        d.append(t*2)
print(array[K])
