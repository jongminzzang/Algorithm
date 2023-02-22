N = int(input())
if N > 379721:
    print(0)

else:
    b = [False for i in range(N+1)]
    prime = []


    for i in range(2,N+1):
        if not b[i]:
            j = 1
            prime.append(i)
            while i*j < N+1:
                b[i*j] = True
                j += 1


    l = []
    for x in prime:
        i = 0
        while x**i <= N:
            i += 1
        l.append(x**(i-1))

    answer = 1
    for x in l:
        answer *= x
        if answer > 987654321:
            answer %= 987654321
    print(answer)