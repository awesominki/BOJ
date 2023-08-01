str = input()
flag = 1
for i in range(len(str) // 2):
    if str[i] != str[len(str)-i-1]:
        flag = 0

print(flag)