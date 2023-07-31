z = int(input())
data = list(map(int, input().split()))
number = int(input())
count = 0
for i in data:
    if i == number:
        count = count + 1
print(count)