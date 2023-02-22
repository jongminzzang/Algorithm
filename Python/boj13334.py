import sys
import heapq

input = sys.stdin.readline
n = int(input())

h = []
for i in range(n):
    x, y = map(int, input().split())
    if y < x:
        x, y = y, x
    heapq.heappush(h, (y, x))

d = int(input())

xh = []
s, e = 0, d
answer, count = 0, 0

while h:
    e = h[0][0]
    s = h[0][0] - d
    while h and h[0][0] <= e:
        ty, tx = heapq.heappop(h)
        if tx >= s:
            heapq.heappush(xh, tx)
            count += 1
    while xh and xh[0] < s:
        heapq.heappop(xh)
        count -= 1
    if count > answer: answer = count

print(answer)
