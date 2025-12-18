import sys

N, X = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

window = sum(data[:X])
best = window
count = 1

for i in range(X, N):
    window += data[i]
    window -= data[i - X]

    if window > best:
        best = window
        count = 1
    elif window == best:
        count += 1

if best == 0:
    print("SAD")
else:
    print(best)
    print(count)
