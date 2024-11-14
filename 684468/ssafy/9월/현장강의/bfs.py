# BFS!!!
#
# DFS와 BFS차이
# 탐색 순서가 다르다
#
# ex) 1차원 리스트 정방향 탐색하던, 역방향 탐색하던 모든 원소를 탐색하는건 같지만,
#     탐색의 순서가 다르다
#
# 즉, BFS는 level 단위로 탐색을 한다.
#
# 자 이제부터 우리는 BFS를 쓰기위해 큐를 쓴다

# 큐 : 선입선출
'''
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(5)
q.append(7)

# n = len(q)
# for i in range(n):
#     print(q[0])
#     q.popleft()

# queue 에서는 for문보다는 while문을 쓰자
# q가 빌 때 까지 반복

while q:
    print(q[0])
    q.popleft()

print(q)
'''

# 문제 16번
# q = [5, 4, 3]
#1. popleft()로 뺀다
#2. *55 + 17 % 11 연산한다
#3. append()로 넣는다
#4. q가 빌때까지 반복(선입선출) - 출력

# from collections import deque
#
# q = deque()
# q.append(5)
# q.append(4)
# q.append(3)
#
# for i in range(5):
#     num = q.popleft()
#     q.append((num*55+17) % 11)
#
# while q:
#     print(q[0])
#     q.popleft()
#====================================================================================
# 문제 17. BFS트리, 인접 리스트
# from collections import deque
#
# alist = [[] for _ in range(7)]
#
# alist[5] = [3, 1]
# alist[3] = [2]
# alist[1] = [4]
# alist[4] = [0, 6]
#
# q = deque()
# q.append(5)
#
# while q:
#     # 1. 큐에서 뺸다(탐색)
#     now = q.popleft()
#     print(now, end=' ')
#     #2. 다음 갈곳 예약 걸기 (큐 등록)
#     for i in range(len(alist[now])):
#         next = alist[now][i]
#         q.append(next)
# # #========================================================================
# #
# from collections import deque
# alist = [[] for _ in range(7)]
# alist[5] = [3,1]
# alist[3] = [2]
# alist[1] = [4]
# alist[4] = [0, 6]
#
# q = deque()
# q.append(5)
#
# while q:
#     now = q.popleft()
#     print(now, end = ' ')
# 문제 18번. 인접행력 BFS탐색

# from collections import deque
# name = 'ACBQTPR'
# table = [[0,1,1,1,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,1,0,0],
#          [0,0,0,0,0,1,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0]]
#
# q = deque()
# q.append(0)
# while q:
#     now = q.popleft()
#     print(name[now],end = ' ')
#
#     for i in range(7): # 노드가 7개
#         if table[now][i] == 0:continue
#         q.append(i)

# 그래프 BFS 탐색
# 트리<--> 그래프 : cycle이 무한루프에 빠질 수 있다.
#===========================================================
# 문제 19. 양방향 그래프BFS탐색 , used배열, 인접 리스트
# from collections import deque
# name = 'ABCDE'
# alist = [[] for _ in range(5)]
# alist[0] = [1, 2]
# alist[1] = [0, 2]
# alist[2] = [0, 1, 3]
# alist[3] = [2, 4]
# alist[4] = [3]
# def bfs(start):
#     q = deque()
#     used = [0] * 10
#     # 항상 start 노드 추가
#     q.append(start)
#     # used 배열 start 방문표시
#     used[start] = 1
#     while q:
#         now = q[0]
#         print(chr(now + ord('A')), end = ' ')
#         q.popleft()
#         for i in range(len(alist[now])):
#             next = alist[now][i]
#             if used[next] == 1: continue
#             used[next] = 1
#             q.append(next)
#
# bfs(0)
# print()
# bfs(3)



#
#
# from collections import deque
#
# MAP = [[qq]]
# q = deque()
# q.append(0)
# while q:
#     now
#
# boss = [0] * 10
# def find(n):
#     if boss[n] == 0:#보스가 없으면
#         return n # n이 최종 보스다
#
#     result = find(boss[n])
#     return result
#
# def union(t1,t2):
#     a = find(t1) # t1의 보스
#     b = find(t2) # t2의 보스
#     if a == b:
#         return  # 같은 보스? 탈락
#     boss[b] = a # b의 보스가 a다
#
# union(6,7)
# union(5,6)
# union(1,2)
#
# if find(2) == find(6):
#     print('같은그룹')
# else:
#     print('다른그룹')
#====================================================
# Union-Find 예제코드2
# boss = [0] * 10
# def find(n):
#     if boss[n] == 0:#보스가 없으면
#         return n # n이 최종 보스다
#
#     result = find(boss[n]) # 0 찾을떄까지 재귀호출
#     boss[n] = result # 코드추가! --> 경로압축
#     return result
#
#
# def union(t1,t2):
#     a = find(t1) # t1의 보스
#     b = find(t2) # t2의 보스
#     if a == b:
#         return  # 같은 보스? 탈락
#     boss[b] = a # b의 보스가 a다
#
# union(6,7)
# union(5,6)
# union(1,2)
#
# if find(2) == find(6):
#     print('같은그룹')
# else:
#     print('다른그룹')

#========================================================
# 문제 21.
# boss = [0] * 10
#
#
# def find(n):
#     if boss[n] == 0 : #보스가 없으면
#         return n # n이 최종 보스다
#
#     result = find(boss[n]) # 0 찾을떄까지 재귀호출
#     boss[n] = result # 코드추가! --> 경로압축
#     return result
#
#
# def union(t1, t2):
#     a = find(t1) # t1의 보스
#     b = find(t2) # t2의 보스
#     if a == b:
#         return  # 같은 보스? 탈락
#     boss[b] = a # b의 보스가 a다
#
# N = int(input())
# for _ in range(N):
#     t1,t2 = map(int,input().split())
#     union(t1, t2)
#
# F = int(input())
# for _ in range(F):
#     f1,f2 = map(int,input().split())
#     if find(f1) == find(f2):
#         print('O')
#     else:
#         print('X')
#
# 4
# 1 3
# 4 2
# 9 5
# 1 4
# 3
# 1 5
# 2 9
# 1 4

# =======================================================
# 암기해라
# 문제 22.cycle 판단코드
# cycle 이 있다.
#: 간선을 한 번씩만 이용했을 때, 제자리로 돌아올 수 있다.
# - cycle 여부 : Union-find 로 알 수 있다. 단, 단방향일때는 안됨. 양방향일때만 가능
# 전략1. 문자를 아스키 코드로 바꾼다.
# 전략2. a와 b가 같은 그룹이면 cycle 발견, 출력!

# boss = [0] * 100
#
#
# def find(n):
#     if boss[n] == 0 : #보스가 없으면
#         return n # n이 최종 보스다
#
#     result = find(boss[n]) # 0 찾을떄까지 재귀호출
#     boss[n] = result # 코드추가! --> 경로압축
#     return result
#
#
# def union(t1, t2):
#     a = find(t1) # t1의 보스
#     b = find(t2) # t2의 보스
#     if a == b:
#         return  # 같은 보스? 탈락
#     boss[b] = a # b의 보스가 a다
#
# n = int(input())
# for _ in range(n):
#     a, b = map(ord, input().split())
#
#     if find(a) == find(b):
#         print('cycle 발견')
#         break
#     else:
#         union(a,b)

# 크루스칼
# def find(n):
#     if boss[n] == 0: return n
#     result = find(boss[n])
#     boss[n] = result
#     return result
#
# def union(t1,t2):
#     a = find(t1)
#     b = find(t2)
#     if a == b:return
#     boss[b] = a
#
# boss = [0] * 100
# members = []
# cnt = 0
# sum_v = 0
#
# n,node = map(int,input().split())
# for _ in range(n):
#     a, b, price = input().split()
#     a, b = ord(a), ord(b) # 문자를 아스키코드로 변경
#     price = int(price)
#     members.append((price,a,b)) # price를 첫 번째 요소로 하여 정렬할 것
# # price를 기준으로 오름차순 정렬
# members.sort()

# for price,a,b in members:
#     if find(a) != find(b):
#         union(a,b)
#         sum_v += price
#         cnt += 1
#         if cnt == node-1: # 모든 노드가 연결 됐다. (n-1 개의 간선)
#             break
# print(sum_v)





# ==============================

# table = [[] for _ in range(6)]
# table[0] = [0,15,0,30,0,0]
# table[1] = [0,0,5,0,0,0]
# table[2] = [0,0,0,6,2,0]
# table[3] = [0,0,0,0,0,7]
# table[4] = [0,0,0,0,0,1]
# table[5] = [0,0,0,0,0,0]
#
# used = [0] * 6
# min_v = float('inf')
# def dfs(now,sum_v):
#     global min_v
#     if now == 5:
#         min_v = min(min_v,sum_v)
#         return
#
#     for i in range(6):
#         if table[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         dfs(i, sum_v + table[now][i])
#         used[i] = 0
#
# #시작노드는 방문처리
# used[0] = 1
# dfs(0,0)
# print(min_v)


# 단점: 느리다,비효율적이다
# ---> 다익스트라 사용 (우선순위 큐 (P.Q))
# ---> 깊이우선 X, 너비우선 X 현재까지 발견 된 가장 저비용 경로를 우선 탐색
from heapq import heappop,heappush
MAP = [[0 for _ in range(6)] for _ in range(6)]

MAP[0][1] = 15
MAP[0][2] = 30
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[3][5] = 7
MAP[4][5] = 1

def dijkstra(start):
    n = len(MAP) # 노드수 6개
    result = [float('inf')]*n
    result[start] = 0 # 시작 노드 초기화
    # 우선순위 큐 초기화
    q = [(0, start)] #거리 , 노드

    while q:
        price, now = heappop(q)
        if result[now] < price: continue

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] # 다음 노드까지의 비용
            price_sum = price + next_price
            if result[i] > price_sum: # 더 적은 비용 경로를 발견하면
                result[i] = price_sum # 최소 비용 업데이트
                heappush((q,(price_sum,i)))
    return result

result = dijkstra(0)
print(f'노드 0부터 최단거리: {result}')
print(f'f 노드 0부터 5까지 최소 비용: {result[5]}')