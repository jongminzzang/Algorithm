import heapq
import sys


input = sys.stdin.readline

N = int(input())

h = []
for x in map(int, input().split()):
    heapq.heappush(h, x)

for i in range(N-1):     
    for x in map(int, input().split()):
        heapq.heappush(h, x)
        heapq.heappop(h)
        
    
print(h[0])

