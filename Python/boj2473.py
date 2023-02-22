import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
l.sort()

answer = (-1, -1, -1)
min_val = 3000000000

for k in range(N):
    # k 번째 용액을 포함하고 나머지 두 용액에 대해서 진행
    a, b = 0, N-1

    while b > a:

        if a == k or b == k:
            a += 1
            continue

        val= l[k] + l[a] + l[b]
        if min_val > abs(val):
            min_val = abs(val)
            answer = (k, a, b)

        if val < 0:
            a += 1
        elif val > 0:
            b -= 1
        else:
            break
a_list = sorted([l[answer[0]], l[answer[1]], l[answer[2]]])
print(a_list[0], a_list[1], a_list[2])