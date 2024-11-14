N, M = map(int, input().split())
V = [1]*N
time = []
for _ in range(M):
    A, B = map(int, input().split())
    time.append((A, B))
time.sort(key=lambda x: x[1])

for a, b in time:
    if V[a-1] >= V[b-1]:
        V[b-1] += V[a-1]

print(*V)