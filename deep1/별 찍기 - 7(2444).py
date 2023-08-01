n = int(input())
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range((i+1)*2-1):
        print("*",end="")
    print()
cnt = 0
for i in range(n-2,-1,-1):
    cnt = cnt + 1
    for j in range(cnt):
        print(" ",end="")
    for j in range((i+1)*2-1):
        print("*",end="")
    print()