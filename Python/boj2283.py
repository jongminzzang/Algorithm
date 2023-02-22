import heapq

N, K = map(int, input().split())

s = [0 for i in range(1000001)]
e = [0 for i in range(1000001)]

max_e = 0
for x in range(N):
    ts, te = map(int, input().split())
    s[ts] +=1
    e[te] += 1
    max_e = max(te, max_e)


A, B = -1, -1
ac, bc = 0, 0
ahaep = []
bheap = []
sum = 0
answer = False
while B < max_e + 1:
    if sum == K:
        answer = True
        break

    # 합이 k 보다 작음 -> B 증가 시켜야함
    elif sum < K:
        B += 1
        sum += bc
        # 끝 점 == B 이면 다음부터 빠져야함
        bc -= e[B]
        # 시작점 == B 이면 다음 부터 더해질 수 잇음
        bc += s[B]

    # 합이 k 보다 큼 -> A를 증가 시켜야함
    elif sum > K:
        A += 1
        sum -= ac
        ac -= e[A]
        ac += s[A]

if answer:
    if A == -1:
        A = 0
    if B == -1:
        B = 0
    print(A, B)
else:
    print(0, 0)