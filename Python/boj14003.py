import bisect
n = int(input())
l = list(map(int, input().split()))
arr = [l[0]]
idx = []

for x in l:
    if arr[-1] < x:
        arr.append(x)
        idx.append(len(arr)-1)
    else:
        k = bisect.bisect_left(arr, x)
        arr[k] = x
        idx.append(k)

answer = []
t = len(arr)-1
for i in range(n-1, -1, -1):
    if idx[i] == t:
        answer.append(l[i])
        t -= 1
    if t == -1:
        break

print(len(answer))
for x in answer[::-1]:
    print(x, end = " ")

