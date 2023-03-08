from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
visit = [False for i in range(N+1)]
l = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
    

q = deque()
q.append(R)
ans = []

for li in l:
    li.sort()


while q:
    x = q.popleft()
    
    # 방문 한 적이 있음
    if visit[x]:
        continue
    
    
    ans.append(x)
    visit[x] = True
    
    for k in l[x][::-1]:
        if not visit[k]:
            q.appendleft(k)



ansArr = [0 for _ in range(N+1)]
for i, a in enumerate(ans):
    ansArr[a] = i+1

for i in range(1, N+1):
    print(ansArr[i])