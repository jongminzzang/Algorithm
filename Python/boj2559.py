N, K = list(map(int, input().split()))
l = list(map(int, input().split()))


answer_list = []
i = 0
j = 0
t = l[j]

while j < N:
    if j - i == K-1:
        answer_list.append(t)
        j += 1
        if j == N:
            break
        t += l[j]
        t -= l[i]
        i += 1

    else:
        j += 1
        t += l[j]

print(max(answer_list))