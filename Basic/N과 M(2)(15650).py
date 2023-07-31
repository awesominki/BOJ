n,m = map(int,input().split())
ans = []

def dfs(num):
    if len(ans) == m:
        print(' '.join(map(str,ans))) #숫자가 들어있는 리스트는 str을 통해 문자로 바꿔서 출력해야함!
        return
    for i in range(num,n+1):
        if i not in ans:
            ans.append(i)
            dfs(i+1)
            ans.pop()


dfs(1)