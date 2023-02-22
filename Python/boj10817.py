a, b, c = map(int, input().split())

if a <= b <= c:
    print(b)
elif c <= b <= a:
    print(b)
elif b <= a <= c:
    print(a)
elif c <= a <= b:
    print(a)
elif a <= c <= b:
    print(c)
elif b <= c <= a:
    print(c)
