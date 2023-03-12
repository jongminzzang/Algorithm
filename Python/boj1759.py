import sys

input = sys.stdin.readline
print = sys.stdout.write

l, c = map(int, input().split())
s = input().split()
s.sort()
mo = set(['a', 'e', 'i', 'o', 'u'])


def dfs(t, a, b, i):
    global l, c

    if a + b == l:
        if a > 0 and b > 1:
            print("%s\n" % t)
        return

    else:
        for j in range(i + 1, c):
            x = t + s[j]
            if s[j] in mo:
                dfs(x, a + 1, b, j)
            else:
                dfs(x, a, b + 1, j)


dfs("", 0, 0, -1)
