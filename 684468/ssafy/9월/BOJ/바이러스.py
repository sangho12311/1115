def dfs(c):
    global ans
    ans += 1
    v[c] = 1
    for n in table[c]:
        if not v[n]:
            dfs(n)


N = int(input())
T = int(input())
table = [[] for _ in range(N+1)]
for i in range(T):
    c1,c2 = map(int,input().split())
    table[c1].append(c2)
    table[c2].append(c1)

ans = 0
v = [0] * (N+1)
dfs(1)
print(ans-1)
