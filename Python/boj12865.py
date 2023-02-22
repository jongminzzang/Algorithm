import sys
input = sys.stdin.readline

N, K = map(int, input().split())

b = []
for x in range(N):
    b.append(list(map(int, input().split())))

dp = []