N = int(input())
arr = [[0 for i in range(10)] for i in range(N+1)]
arr[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for x in range(1, N):
    arr[x][0] = arr[x-1][1]%1000000000
    for j in range(1, 9):
        arr[x][j] = (arr[x-1][j-1] + arr[x-1][j+1])%1000000000
    arr[x][9] = arr[x-1][8]%1000000000

print(sum(arr[N-1])%1000000000)