import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(N)]


# print(arr)

# 가로 합
for i in range(N):
    for j in range(M):
        if j == 0:
            pass
        else:
            arr[i][j] += arr[i][j-1]
# print(arr)
# 세로 합
for i in range(M):
    for j in range(N):
        if j == 0:
            pass
        else:
            arr[j][i] += arr[j-1][i]
# print(arr)



def weighted_sum(i, j, x, y):

    global arr
    i -= 1
    j -= 1

    A = arr[x][y]
    B = 0
    C = 0
    D = 0
    if i >= 0 and j >= 0:
        B = arr[i][j]
    if i >= 0:
        C = arr[i][y]
    if j >= 0:
        D = arr[x][j]
    # print(A, B, C, D)
    return A + B - C - D



K = int(input())
for i in range(K):
    i, j, x, y = list(map(int, input().split()))
    print(weighted_sum(i-1, j-1, x-1, y-1))
