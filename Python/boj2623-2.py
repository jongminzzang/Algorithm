from collections import deque

d = deque()
# N : 가수 1 ~ N
# M : 입력횟수
N, M = map(int, input().split())
s = {i : set() for i in range()}


for _ in range(M):
    l = list(map(int, input().split()))
    k = l.pop(0);


