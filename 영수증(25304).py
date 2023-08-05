total = int(input())
total_number = int(input())
result = 0

for i in range(total_number):
    price,number = map(int,input().split())
    result = result + price*number

if total == result:
    print("Yes")
else:
    print("No")
