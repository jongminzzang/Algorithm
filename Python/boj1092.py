import sys
import bisect
input = sys.stdin.readline
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
b = [True for _ in range(M)]

n.sort()
m.sort()

if m[-1] > n[-1]:
    print(-1)
else:
    k = []
    for x in n:
        i = bisect.bisect(m, x)-1
        if i >= 0:
            k.append(i)
    count = 0
    t = 0
    while k:
        t += 1
        new_k = []

        for x in k:
            while True:
                if x < 0:
                    break
                if b[x]:
                    b[x] = False
                    count += 1
                    if x > 0:
                        new_k.append(x-1)
                    break
                x -= 1
        if count >= M:
            break
        k = new_k
    print(t)