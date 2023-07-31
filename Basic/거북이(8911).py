import sys

way = 0 # 0:북, 1:동, 2:남, 3:서
x = [0]
y = [0]
j = 0
k = 0

t = int(input())
for _ in range(t):
    order = list(map(str, sys.stdin.readline().strip()))
    for i in order:
        if i == "F":
            if way == 0:
                y.append(y[j]+1)
                j += 1
            elif way == 1:
                x.append(x[k]+1)
                k += 1
            elif way == 2:
                y.append(y[j]-1)
                j += 1
            elif way == 3:
                x.append(x[k]-1)
                k += 1

        elif i == "B":
            if way == 0:
                y.append(y[j] - 1)
                j += 1
            elif way == 1:
                x.append(x[k] - 1)
                k += 1
            elif way == 2:
                y.append(y[j] + 1)
                j += 1
            elif way == 3:
                x.append(x[k] + 1)
                k += 1

        elif i == "L":
            if way == 3:
                way = 0
            else:
                way += 1

        elif i == "R":
            if way == 0:
                way = 3
            else:
                way -= 1

    print(abs(max(x)-min(x)) * abs(max(y)-min(y)))
    j = 0
    k = 0
    way = 0
    x.clear()
    y.clear()
    x = [0]
    y = [0]