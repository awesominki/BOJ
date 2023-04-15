from itertools import combinations_with_replacement

n = int(input())
cnt = 0
roma_num = [1, 5, 10, 50]
result = set()
sum = 0

for i in combinations_with_replacement(roma_num,n):
    for j in range(n):
        sum += i[j]
    result.add(sum)
    sum = 0


print(len(result))