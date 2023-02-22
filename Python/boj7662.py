import heapq
import sys

input = sys.stdin.readline

T = int(input())
answer = []


for _ in range(T):
    k = int(input())

    h_len = 0
    min_h = []
    max_h = []
    min_s = {}
    max_s = {}

    for i in range(k):
        x, y = input().split()
        y = int(y)

        # insert
        if x == 'I':
            heapq.heappush(min_h, y)
            heapq.heappush(max_h, -y)
            h_len += 1

        # Delete
        else:
            # if queue Empty
            if h_len <= 1:
                h_len = 0
                min_h = []
                max_h = []
                min_s = {}
                max_s = {}

            # Delete Max
            elif y == 1:
                while True:
                    t = -heapq.heappop(max_h)

                    # Delete already by min
                    if t in max_s and max_s[t]:
                        max_s[t] -= 1

                    # Delete now
                    else:
                        if t in min_s:
                            min_s[t] += 1
                        else:
                            min_s[t] = 1
                        h_len -= 1
                        break

            # Delete Min
            else:
                while True:
                    t = heapq.heappop(min_h)

                    if t in min_s and min_s[t]:
                        min_s[t] -= 1

                    else:
                        if t in max_s:
                            max_s[t] += 1
                        else:
                            max_s[t] = 1
                        h_len -= 1
                        break

    if h_len == 0:
        answer.append("EMPTY")
    elif h_len == 1:
        while True:
            t = -heapq.heappop(max_h)

            # Delete already
            if t in max_s and max_s[t]:
                max_s[t] -= 1

            # Delete now
            else:
                if t in min_s:
                    min_s[t] += 1
                else:
                    min_s[t] = 1
                break
        max_a = t
        answer.append((max_a, max_a))
    else:
        while True:
            t = -heapq.heappop(max_h)

            # Delete already
            if t in max_s and max_s[t]:
                max_s[t] -= 1

            # Delete now
            else:
                if t in min_s:
                    min_s[t] += 1
                else:
                    min_s[t] = 1
                break
        max_a = t
        while True:
            t = heapq.heappop(min_h)

            if t in min_s and min_s[t]:
                min_s[t] -= 1
                continue

            else:
                if t in max_s:
                    max_s[t] += 1
                else:
                    max_s[t] = 1
                break
        min_a = t
        answer.append((max_a, min_a))

for x in answer:
    if x == "EMPTY":
        print(x)
    else:
        print(x[0], x[1])