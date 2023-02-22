from collections import deque
import sys

input = sys.stdin.readline
d = deque()

R, C, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]
x = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def circulate(x):
    global R, C, m
    #위쪽

    mx, my = x[0][0], x[0][1]
    for i in range(mx - 1, 0, -1):
        m[i][0] = m[i - 1][0]
    for i in range(1, C):
        m[0][i - 1] = m[0][i]
    for i in range(1, mx+1):
        m[i - 1][C - 1] = m[i][C - 1]
    m[mx][2:C] = m[mx][1:C - 1]
    m[mx][1] = 0

    # 아래쪽
    mx, my = x[1][0], x[1][1]
    for i in range(mx+2, R):
        m[i-1][0] = m[i][0]
    m[R-1][0:C-1] = m[R-1][1:]
    for i in range(R-1, mx, -1):
        m[i][C-1] = m[i-1][C-1]
    m[mx][2:C] = m[mx][1:C - 1]
    m[mx][1] = 0


def print_map(m):
    for k in m:
        print(k)

# print(sum([sum(i) for i in m]))
for i in range(R):
    for j in range(C):
        if m[i][j] == 0:
            pass
        elif m[i][j] != -1:
            d.append((i,j,m[i][j]))
        else:
            x.append((i,j))
# print(x)



for t in range(T):
    # print(t, sum([sum(i) for i in m]))
    # print()

    # 먼지 확산
    new_map = [[0 for _ in range(C)] for _ in range(R)]
    new_map[x[0][0]][x[0][1]]  = -1
    new_map[x[1][0]][x[1][1]] = -1

    while d:
        tx, ty, tm = d.popleft()
        cnt = 0
        for i in range(4):
            ttx = tx + dx[i]
            tty = ty + dy[i]
            if ttx > -1 and tty > -1 and ttx < R and tty < C and new_map[ttx][tty] != -1:
                new_map[ttx][tty] += tm//5
                cnt += 1
        new_map[tx][ty] += tm - (tm//5)*cnt
    m = new_map
    circulate(x)

    # deque에 집어 넣기
    for i in range(R):
        for j in range(C):
            if m[i][j] == 0:
                pass
            elif m[i][j] != -1:
                d.append((i, j, m[i][j]))

print(sum(sum(m,[]))+2)