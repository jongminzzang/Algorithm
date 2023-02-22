import sys

input = sys.stdin.readline
N = int(input())
d1 = {}
d2 = {}

for x in range(N):
    a, b, c, d = map(int, input().split())
    if a + b in d1:
        d1[a+b] += 1
    else:
        d1[a+b] = 1
    if c + d in d2:
        d2[c+d] += 1
    else:
        d2[c+d] = 1


answer = 0
for x in d1:
    if -x in d2:
        answer += d1[x]*d2[-x]

print(answer)
