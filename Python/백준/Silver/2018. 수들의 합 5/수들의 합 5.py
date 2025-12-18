import sys


N = int(sys.stdin.readline())


left = 1
right = 1
count = 0
total = 1


while True:
    if total>N:
        total -= left
        left += 1
    elif total == N:
        count += 1
        total -= left
        left += 1
    else:
        right +=1
        if  right > N:
            break
        total += right

        
print(count)