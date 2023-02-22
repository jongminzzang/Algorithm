import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0

for i in range(N):
    a, b = i-1, i+1

    while a > -1 and b < N:
        t = A[i] + A[a] + A[b]

        if t < 0:
            b += 1
        elif t > 0:
            a -= 1
        else:
            next_to_a = 1
            while True:
                if a -1 == -1:
                    break
                if A[a] == A[a-1]:
                    a -= 1
                    next_to_a += 1
                else:
                    break

            next_to_b = 1
            while True:
                if b + 1 == N:
                    break

                if A[b] == A[b+1]:
                    b += 1
                    next_to_b +=1
                else:
                    break
            a -= 1
            answer += (next_to_a*next_to_b)


print(answer)
