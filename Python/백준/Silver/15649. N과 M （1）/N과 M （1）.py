import sys

N, M = map(int, sys.stdin.readline().split())

data = [0] * (N+1)

for i in range(1,N):
    data[i] = i
    
check = [0] * (N+1)

tmp = []

def func(arr,K,M):
    if K == M:
        print(*tmp)
        return
    for i in range(1,N+1):
        if check[i]:
            continue
        else:
            check[i] = 1
            tmp.append(i)
            func(arr, K+1, M)
            check[i] = 0
            tmp.pop()
            
func(data,0,M)

        



