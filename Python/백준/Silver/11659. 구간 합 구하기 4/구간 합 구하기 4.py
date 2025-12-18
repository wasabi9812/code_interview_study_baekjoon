import sys

N, M = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
pre_data = [0] * N 
pre_data[0] = data[0]
for i in range(1, N):
    pre_data[i] = data[i] + pre_data[i-1]


    
for i in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    a -= 1
    b -= 1
    if a ==0:
        print(pre_data[b])
    else:
        print(pre_data[b] - pre_data[a-1])