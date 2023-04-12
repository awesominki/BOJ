n,m = map(int,input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(' '.join(map(str,ans))) #숫자가 들어있는 리스트는 str을 통해 문자로 바꿔서 출력해야함!
        return
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()


dfs()