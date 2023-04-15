from collections import deque

n,m = map(int, input().split())
queue=deque([i for i in range(1,n+1)])
col = list(map(int,input().split()))
cnt = 0

for i in col:
    while True:
        if queue[0] == i:
            queue.popleft()
            break

        else:
            if (len(queue) - queue.index(i)) > queue.index(i):
                queue.append(queue.popleft())
            else:
                queue.appendleft(queue.pop())

            cnt += 1

print(cnt)