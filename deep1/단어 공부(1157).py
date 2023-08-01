str = input()
list = [0 for i in range(26)]
str = str.upper()

for i in str:
    s = ord(i)
    list[s-65] = list[s-65] + 1

sorted_list = list.copy()
sorted_list.sort(reverse=True)

if sorted_list[0] == sorted_list[1]:
    print("?")
else:
    print(chr(list.index(max(list))+65))