N = int(input())
if N == 1:
    print(0)
else:
    b = [False for i in range(N+1)]
    prime = []

    for i in range(2, int(N**0.5) + 2):
        j = 2
        if not b[i]:
            while i*j <= N:
                b[i*j] = True
                j += 1

    for i in range(2, N+1):
        if not b[i]:
            prime.append(i)


    i, j = 0, 0
    t = prime[0]
    answer = 0

    while True:
        if t < N:
            j += 1
            if j < len(prime):
                t += prime[j]
        elif t > N:
            t -= prime[i]
            i += 1
        else:
            answer += 1
            j += 1
            if j < len(prime):
                t += prime[j]

        if j == len(prime):
            break


    print(answer)