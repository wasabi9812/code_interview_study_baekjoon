import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

min_n = data[0]
max_n = data[0]

for i in range(1, N):
    if data[i] < min_n:
        min_n = data[i]
    if data[i] > max_n:
        max_n = data[i]

print(min_n, max_n)