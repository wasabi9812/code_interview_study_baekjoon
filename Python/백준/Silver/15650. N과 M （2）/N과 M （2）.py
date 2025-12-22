import sys

N, M = map(int, sys.stdin.readline().split())

tmp = []

def dfs(start, k):
    if k == M:
        print(*tmp)
        return
    for i in range(start, N + 1):
        tmp.append(i)
        dfs(i + 1, k + 1)
        tmp.pop()

dfs(1, 0)