N, K = map(int, input().split())

prime = []

t = [0 for i in range(N + 1)]

for i in range(2, N + 1):
    j = 1
    if t[i] == 0:
        prime.append(i)
        while j * i <= N:
            t[j * i] = 1
            j += 1
print(prime)
val = [0 for i in range(len(prime))]

# if K * 2 > N:
#     K = N - K
#
#
# def plus_prime(x):
#     global prime, val
#     for i, p in enumerate(prime):
#         if x == 1:
#             break
#         while x % p == 0:
#             x //= p
#             val[i] += 1
#
#
# def minus_prime(x):
#     global prime, val
#     for i, p in enumerate(prime):
#         if x == 1:
#             break
#         while x % p == 0:
#             x //= p
#             val[i] -= 1
#
#
# for i in range(N, N - K, -1):
#     plus_prime(i)
# for i in range(K, 1, -1):
#     minus_prime(i)
#
# answer = 1
# for i in range(len(prime)):
#     if val[i] != 0:
#         for j in range(val[i]):
#             answer *= prime[i]
#             if answer > 1000000007:
#                 answer = answer % 1000000007
#
# print(answer)
