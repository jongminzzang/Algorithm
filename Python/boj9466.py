import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())

for t in range(T):
    k = int(input())

    team = [0 for i in range(k+1)]
    l = [0]+list(map(int, input().split()))

    index = 1
    for i in range(1, k+1):
        # 이미 순환이 있는지 검사가 끝남
        if team[i] != 0:
            continue
        # 혼자서 팀
        elif l[i] == i:
            team[i] = i
            team[i] = index
            index += 1
        # 순환 돌려봐야함
        else:
            s = set()
            t = i
            circle = True

            while True:
                s.add(t)
                # 순환 존재 못함 확인
                if team[l[t]] != 0:
                    for v in s:
                        team[v] = -1
                    circle = False
                    break
                # 순환 발견
                elif l[t] in s:
                    break
                else:
                    t = l[t]
            if circle:
                start = l[t]
                while True:
                    team[t] = index
                    t = l[t]
                    if l[t] == start:
                        break
                index += 1
                for z in s:
                    if team[z] == 0:
                        team[z] = -1
    c = Counter(team)
    print(c[-1])