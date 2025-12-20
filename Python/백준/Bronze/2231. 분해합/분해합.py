import sys

N = int(sys.stdin.readline())

min_num = 100000000000
for i in range(1, N):
    tmp = i
    tmp2 = i
    ten_cnt =1
    while tmp2 >= 10:
        ten_cnt += 1
        tmp2= tmp2//10
    sn = str(tmp)
    for j in range(ten_cnt):
        tmp +=int(sn[j])
    if tmp == N:
        if min_num > i:
            min_num = i
if min_num == 100000000000:
    print(0)
else:
    print(min_num)
        