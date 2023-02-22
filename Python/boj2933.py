from collections import deque

R, C = map(int, input().split())
m = [list(input()) for i in range(R)]
visit = [[0 for i in range(C)] for i in range(R)]

N = int(input())
l = list(map(int, input().split()))


def throw(i, height):
    global m, R, C
    if i % 2 == 0:
        for j in range(C):
            if m[R - h][j] == 'x':
                m[R - h][j] = '.'
                return R - h, j
    elif i % 2 == 1:
        for j in range(C - 1, -1, -1):
            if m[R - h][j] == 'x':
                m[R - h][j] = '.'
                return R - h, j
    return -1, -1


def get_cluster(r, c, v):
    global m, R, C, visit
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = deque()
    s = set()

    if v == 'u':
        r -= 1
    elif v == 'l':
        c -= 1
    elif v == 'r':
        c += 1
    elif v == 'd':
        r += 1
    visit[r][c] == 1
    d.append((r, c))
    s.add((r, c))

    while d:
        tx, ty = d.popleft()
        for i in range(4):
            ttx = tx + dx[i]
            tty = ty + dy[i]
            if 0 <= ttx < R and 0 <= tty < C and visit[ttx][tty] == 0 and m[ttx][tty] == 'x':
                if ttx == R - 1:
                    for k in s:
                        visit[k[0]][k[1]] = 0
                    return set()
                visit[ttx][tty] = 1
                d.append((ttx, tty))
                s.add((ttx, tty))

    for t in s:
        visit[t[0]][t[1]] = 0
    return s


def drop(s):
    if not s:
        return
    global m
    for x in s:
        m[x[0]][x[1]] = '.'

    max_move = R + 1
    for x in s:
        i = 0;
        while i <= max_move:
            if x[0]+i == R or m[x[0]+i][x[1]] == 'x':
                max_move = i
                break
            i += 1
        if max_move == 2:
            break
    for x in s:
        m[x[0]+max_move-1][x[1]] = 'x'


for i, h in enumerate(l):
    union_set = set()
    x, y = throw(i, h)

    if x == -1:
        continue

    # left or right
    if i % 2 == 0:
        if y != C-1 and m[x][y+1] == 'x':
            union_set = get_cluster(x, y, 'r')
    elif i % 2 == 1:
        if y != 0 and m[x][y - 1] == 'x':
            union_set = get_cluster(x, y, 'l')
    # up
    if len(union_set) == 0 and x != 0 and m[x-1][y] == 'x':
        union_set = up = get_cluster(x, y, 'u')
    # down
    if len(union_set) == 0 and x != R - 1 and m[x + 1][y] == 'x':
        union_set = up = get_cluster(x, y, 'd')

    drop(union_set)


for x in m:
    print(''.join(x))