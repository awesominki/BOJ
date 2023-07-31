n,m = map(int,input().split())
list = [0 for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())

    for j in range(a-1,b):
        list[j] = c

print(*list)