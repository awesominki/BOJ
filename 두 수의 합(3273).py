n = int(input())
number = list(map(int,input().split()))
flag = int(input())

number.sort()
start = 0
end = n-1
cnt = 0

while start < end :
    if number[start] + number[end] == flag:
        cnt += 1
    if number[start] + number[end] < flag :
        start += 1
        continue
    end -= 1

print(cnt)