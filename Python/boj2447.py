n = int(input())
k = [[' ' for _ in range(n)] for _ in range(n)]

def func(N, a, b):
    global k
    if N == 1:
        k[a][b]  = '*'
    else:
        NN = N//3
        func(NN, a, b)
        func(NN, a, b+NN)
        func(NN, a, b+2*NN)
        func(NN, a+NN, b)
        func(NN, a+NN, b+2*NN)
        func(NN, a+2*NN, b)
        func(NN, a + 2*NN, b+NN)
        func(NN, a + 2*NN, b+2*NN)

func(n, 0, 0)

for x in k:
    for y in x:
        print(y, end="")
    print("")