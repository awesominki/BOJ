n,m = map(int, input().split())
list = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    list[a-1],list[b-1] = list[b-1],list[a-1]
print(*list)