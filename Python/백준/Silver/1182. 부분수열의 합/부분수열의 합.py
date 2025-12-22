import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

pos_cnt = 0
tmp = []

def dfs(start, cur_sum):
    global pos_cnt

    if cur_sum == M and tmp:
        pos_cnt += 1

    for i in range(start, N):
        tmp.append(data[i])
        dfs(i + 1, cur_sum + data[i])
        tmp.pop()

dfs(0, 0)
print(pos_cnt)
