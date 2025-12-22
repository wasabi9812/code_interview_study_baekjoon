import sys


N = int(sys.stdin.readline())


tmp = []
check = [0] *(N+1)

def func(k):
    if k == N:
        print(*tmp)
        return
    for i in range(1,N+1):
        if check[i]:
            continue
        else:
            check[i] = 1
            tmp.append(i)
            func(k+1)
            tmp.pop()
            check[i] = 0
            
func(0)