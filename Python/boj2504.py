from collections import deque


d = deque()
s = input()
m = [0 for i in range(len(s))]
answer = 0
b = True

for x in s:
    if x == '(':
        d.append("(")

    elif x == ")":
        if not d:
            b = False
            break

        t = d.pop()
        if t != "(":
            b = False
            break
        else:
            l = len(d)
            if m[l+1] == 0:
                m[l] += 2
            else:
                m[l] += m[l+1] *2
                m[l+1] = 0

    elif x == '[':
        d.append("[")

    elif x == "]":
        if not d:
            b = False
            break

        t = d.pop()
        if t != "[":
            b = False
            break
        else:
            l = len(d)
            if m[l + 1] == 0:
                m[l] += 3
            else:
                m[l] += m[l + 1] * 3
                m[l + 1] = 0

    # print(x, m, d)
    if not d:
        answer += m[0]
        m[0] = 0

if b:
    print(answer)
else:
    print(0)
