list = [0 for i in range(42)]
count = 0
for i in range(10):
    n = int(input())
    list[n%42] = list[n%42] + 1

for i in list:
    if i >= 1:
        count = count + 1

print(count)