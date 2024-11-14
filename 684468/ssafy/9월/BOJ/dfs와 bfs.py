from collections import deque

N, M, V = map(int, input().split())
table = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    table[x][y] = 1
    table[y][x] = 1

v1 = [0] * (N+1)
v2 = [0] * (N+1)

def dfs(n):
    v1[n] = True
    print(n, end=' ')
    for i in range(1,N+1):
        if v1[i] == 0 and table[n][i] == 1:
            dfs(i)
dfs(V)

def bfs(n):
    q = deque([n])
    v2[n] = 1
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in range(1, N+1):
            if v2[i] == 0 and table[n][i] == 1:
                q.append(i)
                v2[i] = 1
print()
bfs(V)