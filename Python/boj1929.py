K, N = map(int, input().split())

prime = []

t = [0 for i in range(N + 1)]

for i in range(2, N + 1):
    j = 1
    if t[i] == 0:
        if i >= K:
            print(i)
        prime.append(i)
        while j * i <= N:
            t[j * i] = 1
            j += 1
# print(prime)