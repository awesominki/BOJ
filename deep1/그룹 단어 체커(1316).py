n = int(input())
result = 0

for i in range(n):
    check = 1
    str = input().upper()
    list = [0 for k in range(26)]
    for j in range(len(str)):
        for l in range(j+1,len(str)):
            if str[j] == str[l]:
                break
            else:
                list[ord(str[j]) - 65] = list[ord(str[j]) - 65] + 1
                break
        if list[ord(str[j])-65] == 2 or j == l:
            check = 0
            break

    if check == 1:
        result = result + 1
print(result)



