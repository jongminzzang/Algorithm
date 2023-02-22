from collections import Counter

r, c, k = map(int, input().split())
l = []
for x in range(3):
    l.append(list(map(int, input().split())))


def R(A):
    new_A = []
    for i, x in enumerate(A):
        t = []
        counter = Counter(x)
        for v in counter:
            t.append((v, counter[v]))
            # 등장횟수 오름차순, 수 오름차순
            t.sort(key = lambda x:(x[1], x[0]))
        A[i] = []
        ta = []
        for v in t:
            if v[0] == 0:
                continue
            ta.append(v[0])
            ta.append(v[1])
        if len(t) == 100:
            break
        new_A.append(ta)

    # 0 채우기
    max_len = len(max(new_A, key = lambda x : len(x)))
    for x in new_A:
        x += [0]*(max_len - len(x))
    if len(new_A) > 100:
        new_A = new_A[:100]
    return new_A

def C(A):
    A = list(map(list, zip(*A)))
    A = R(A)
    A = list(map(list, zip(*A)))
    return A

def P(A):
    for x in A:
        print(x)
    print()

answer = 0
t = 0
# P(l)
while True:
    # 종료 조건
    if len(l[0]) > 100 or len(l) > 100 or answer > 100:
        answer = -1
        break
    elif r <= len(l) and c <= len(l[0]) and l[r-1][c-1] == k:
        break
    else:
        answer += 1

    # 행의 개수 len(l)
    # 열의 개수 len(l[0])
    if len(l) >= len(l[0]):
        l = R(l)
    else:
        l = C(l)
    # P(l)

print(answer)