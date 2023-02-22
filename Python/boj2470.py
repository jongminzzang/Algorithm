N = int(input())
d = list(map(int, input().split()))
d.sort()
l, r = 0, N-1
min_now = 2000000001
answer_l, answer_r = d[0], d[N-1]

while l < r:
    
    t = d[l]+d[r]
    
    if t == 0:
        answer_l, answer_r = d[l], d[r]
        break
    elif t < 0:
        if abs(t) < min_now:
            min_now = abs(t)
            answer_l, answer_r = d[l], d[r]
        l += 1

    elif t > 0:
        if abs(t) < min_now:
            min_now = abs(t)
            answer_l, answer_r = d[l], d[r]
        r -= 1

print(answer_l, answer_r)
