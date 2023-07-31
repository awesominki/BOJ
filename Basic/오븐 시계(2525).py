hour, minute = map(int,input().split())

num = int(input())

total = minute + num

while(1) :
    if(total < 60) :
        if(hour>=24):
            hour -= 24
        print(hour, total)
        break
    elif(total >= 60) :
        hour += 1
        total -= 60