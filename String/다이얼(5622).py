str = input()
result = 0
for i in range(len(str)):
    if str[i] in "ABC":
        result = result + 3
    elif str[i] in "DEF":
        result = result + 4
    if str[i] in "GHI":
        result = result + 5
    if str[i] in "JKL":
        result = result + 6
    if str[i] in "MNO":
        result = result + 7
    if str[i] in "PQRS":
        result = result + 8
    if str[i] in "TUV":
        result = result + 9
    if str[i] in "WXYZ":
        result = result + 10
print(result)