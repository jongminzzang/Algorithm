N, r, c = map(int, input().split())
answer = 0

t = 2**(N-1)

while t >= 1:

    rr, cc = 0, 0
    if r >= t:
        r = r-t
        rr = 1

    if c >= t:
        c = c-t
        cc = 1

    if rr == 1 and cc == 1:
        answer += 3*t*t
    elif rr == 1:
        answer += 2*t*t
    elif cc == 1:
        answer += t*t

    t //= 2

print(answer)