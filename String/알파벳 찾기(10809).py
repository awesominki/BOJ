str = input()
alpha = "A"

for i in range(97,123):
    cnt = 0
    for j in range(len(str)):
        if str[j] == chr(i):
            print(j,end=" ")
            cnt = cnt + 1
            break
    if cnt == 0:
        print(-1,end=" ")
