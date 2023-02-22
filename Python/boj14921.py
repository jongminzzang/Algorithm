import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))

a, b = 0, N-1
answer = (-1, -1)
m = 2000000000

while a < b:
    t = l[a] + l[b]

    # 최소값 갱신
    if abs(t) < abs(m):
        m = t
        answer = (a, b)

    if t > 0:
        b -= 1
    elif t < 0:
        a += 1
    else:
        break

print(m)