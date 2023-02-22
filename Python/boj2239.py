from collections import deque

m = []
d = deque()
g_map = [[[] for _ in range(9)] for _ in range(9)]

for i in range(9):
    s = list(input())
    t = []
    for j in range(9):
        t.append(int(s[j]))
        if s[j] == '0':
            g_map[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            d.append((i, j))
    m.append(t)

#
# def check(i, j){
#     if i
# }
#
# while d:
#
#

