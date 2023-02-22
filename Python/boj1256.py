# N 개의 a
# M 개의 z
# K 번 째 문자열을 구하시오
from itertools import combinations

N, M, K = map(int, input().split())


# 전체 경우의 수
# N+M C
# N+M-1 C M

# a+b C s
def combi(a, b):
    if a == 0 or b == 0:
        return 1

    s = min(a,b)
    t = a+b
    mul = 1
    div = 1

    for i in range(s, 0, -1):
        mul *= t
        if mul % i == 0:
            mul //= i
        else:
            div *= i
        if div != 1 and mul % div == 0:
            mul //= div
            div = 1
        t -= 1
    return mul


answer = ""
while N + M:
    if combi(N,M) < K:
        answer += "-1"
        break
    if N == 0:
        answer += "z"*M
        break
    elif M == 0:
        answer += "a"*N
        break

    # z가 와야되는 경우
    if  K > combi(N-1, M):
        answer += "z"
        K -= combi(N-1, M)
        M -= 1
    # a가 와야되는 경우
    elif K <= combi(N-1, M):
        answer += "a"
        N -= 1


print(answer)