import sys

input = sys.stdin.readline

T = int(input())
n = int(input())
N = list(map(int, (input().split())))
m = int(input())
M = list(map(int, (input().split())))
#
# if n > m:
#     n, m = m, n
#     N, M = M, N

d = dict()
for i in range(n):
    s = 0
    for j in range(i, n):
        s += N[j]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

e = dict()
for i in range(m):
    s = 0
    for j in range(i, m):
        s += M[j]
        if s in e:
            e[s] += 1
        else:
            e[s] = 1

answer = 0
for x in d:
    if T-x in e:
        answer += d[x]*e[T-x]

print(answer)