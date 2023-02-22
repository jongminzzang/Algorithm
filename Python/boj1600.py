from collections import deque


K = int(input())
W, H = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ddx = [-2, -2, -1, -1, 1, 1, 2, 2]
ddy = [1, -1, 2, -2, 2, -2, 1, -1]

m = []
for x in range(H):
    m.append(list(map(int, input().split())))

visit = [[[-1 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]
visit[0][0][0] = 0

d = deque()
d.append((0, 0, 0))
answer = 50000

while d:
    t = d.popleft();
    tx = t[0]
    ty = t[1]
    tk = t[2]

    c = visit[tx][ty][tk]

    for i in range(4):
        ttx = tx + dx[i]
        tty = ty + dy[i]

        if 0 <= ttx < H and 0 <= tty < W and m[ttx][tty] == 0:
            if visit[ttx][tty][tk] == -1:
                visit[ttx][tty][tk] = c + 1
                d.append((ttx, tty, tk))
                if ttx == H - 1 and tty == W - 1:
                    answer = min(answer, c + 1)

    if tk < K:
        for i in range(8):
            ttx = tx + ddx[i]
            tty = ty + ddy[i]

            if 0 <= ttx < H and 0 <= tty < W and m[ttx][tty] == 0:
                if visit[ttx][tty][tk+1] == -1:
                    visit[ttx][tty][tk+1] = c + 1
                    d.append((ttx, tty, tk + 1))
                    if ttx == H - 1 and tty == W - 1:
                        answer = min(answer, c + 1)


answer = 50000
for x in visit[H-1][W-1]:
    if x == -1:
        pass
    else:
        answer = min(answer, x)

if answer == 50000:
    print(-1)
else:
    print(answer)