m = [
    list("###...#.###.###.#.#.###.###.###.###.###"),
    list("#.#...#...#...#.#.#.#...#.....#.#.#.#.#"),
    list("#.#...#.###.###.###.###.###...#.###.###"),
    list("#.#...#.#.....#...#...#.#.#...#.#.#...#"),
    list("###...#.###.###...#.###.###...#.###.###")
]
tow = []


def f(start):
    global tow, m
    l = []
    for i in range(0, 10):
        b = True
        for j in range(5):
            for k in range(3):
                if tow[j][start + k] == '#' and m[j][4 * i + k] == '.':
                    b = False
                    break
            if not b:
                break
        if b:
            l.append(i)
    return l


N = int(input())

for i in range(5):
    tow.append(list(input()))

answer = 0

for i in range(N):
    t = f(4 * i)
    if len(t) == 0:
        answer = -1
        break
    else:
        answer += sum(t) / len(t) * 10 ** (N - i - 1)

print(answer)