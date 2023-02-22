from collections import deque

R, C = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, -0]

m = []
for _ in range(R):
    t = list(input())
    t = list(map(ord, t))
    m.append(t)

s = [0]*26
s[m[0][0] - 65] = 1

d = deque()
d.append((0, 0, s, 1))

answer = 0
while d:
    t = d.popleft()
    if t[3] > answer:
        answer = t[3]
    for k in range(4):
        tx = t[0] + dx[k]
        ty = t[1] + dy[k]
        if 0 <= tx < R and 0 <= ty < C:
            if t[2][m[tx][ty]-65]:
                pass
            else:
                new_s = t[2][:]
                new_s[m[tx][ty] - 65] = 1
                d.append((tx, ty, new_s, t[3]+1))

print(answer)