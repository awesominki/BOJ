n,m = map(int, input().split())
list = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    tmp = list[a-1:b]
    tmp.reverse()
    for j in tmp:
        list[a-1] = j
        a = a + 1

print(*list)