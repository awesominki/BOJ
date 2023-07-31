from collections import Counter

word = list(input())
word.sort()
wordCounter = Counter(word)
cnt = 0
center = ""
front = ""

for i in wordCounter:
    if wordCounter[i]%2==1:
        cnt+=1
        center+=i
        word.remove(i)

if cnt >= 2:
    print("I'm Sorry Hansoo")

else:
    for i in range(0,len(word),2):
        front += word[i]
    print(front + center + front[::-1])