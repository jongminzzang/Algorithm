from collections import deque

t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = []

for _ in range(t):
    s = set([0])
    M, N, k = map(int , input().split())
    m = [[0 for _ in range(M)] for _ in range(N)]
    d = deque()

    for i in range(1, k+1):
        y, x = map(int, input().split())
        m[x][y] = i
        d.append((x,y))

    while d:
        x, y = d.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx > N-1 or ty < 0 or ty > M-1:
                pass
            elif m[tx][ty] > m[x][y]:
                m[tx][ty] = m[x][y]
                d.append((tx,ty))
    
    for row in m:
        for val in row:
            if val not in s:
                s.add(val)
    answer.append(len(s)-1)


for x in answer:
    print(x)