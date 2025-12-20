import sys
2
n = sys.stdin.readline()
n = int(n)
    
for i in range(1,10):
    print(str(n)+" * "+str(i)+" = "+str(i*n))