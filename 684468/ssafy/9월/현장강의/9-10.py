# 문제1. 그래프와 인접행렬
# name = 'BTAR'
# MAP = [[0, 0, 0, 0],
#        [1, 0, 0, 0],
#        [1, 1, 0, 0],
#        [1, 1, 0, 0]]
#
# n = int(input())
# for i in range(4):
#         # if MAP[n][i] == 1: print(name[i])
#         if MAP[n][i] == 0 :continue
#         print(name[i])
# ======================================

# 문제2 그래프와 인접행렬2
# name = 'ABCDE'
# MAP = [[0, 1, 0, 0, 0],
#        [0, 0, 1, 1, 0],
#        [0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0]]
#
# ch = input()
# n = ord(ch) - ord('A')
# for i in range(5):
#     if MAP[n][i] == 0: continue
#     print(chr(i + ord('A')))

# ==============================================
# 문제3. 2차원 배열과 append 1

# m = [] # 빈 배열을 만들고 append만 사용해섯 [[3,5],[]] 출력
# m.append([3, 5])
# m.append([])
# print(m)

# ==============================================
# 문제4. 2차원 배열과 append 2
# lst = [[]for _ in range(4)]
# lst[0].append(4)
# lst[0].append(2)
# lst[0].append(5)
# lst[0].append(1)
# lst[0].append(1)
# lst[1].append(3)
# lst[1].append(4)
# lst[1].append(2)
# lst[3].append(1)
# lst[3].append(1)
# lst[3].append(2)
# lst[3].append(3)

# for i in lst: # m 2차원 리스트를 순회하면 i는 1차원 리스트
# print(i)

# Q) 모든 원소를 출력하고싶다.
# for y in range(len(lst)):
#     for x in range(len(lst[y])):
#         print(lst[y][x], end='')
#     print()

# 문제5. 2차원 배열을 역순으로 출력(2차원 배열은 하드코딩)

# m = [['A', 'B', 'T'], [], ['R', 'S']]
# for y in range(len(m)):
#     for x in range(len(m[y]) - 1, -1, -1):  # 0까지 1씩 감소
#         print(m[y][x], end='')
#     print()
# ===========================================================================
# 인접리스트와 인접행렬(비어있는게 모두 0으로 채워져 있다.)의 차이
# 메모리 공간 : 인접리스트<인접행렬 (인접리스트가 공간복잡도가 더 좋다)
# 입력데이터에 따라 인접행렬이 더 편할 때가 있고, 인접 리스트가 더 편할 때가 있다.

# alist = list([] for _ in range(4))
# alist[1] = [0, 3]
# alist[2] = [1, 3]
#
# print(alist)
# =======================================================================
# 문제 6
# # 인접 리스트를 하드코딩하고 n을 입력받을 때, name을 출력
# alist = list([] for _ in range(5))
# name = 'DUSRK'
# alist[0] = [1,3,4]
# alist[1] = [2,3]
# alist[3] = [2,4]
# alist[4] = [1,3]
#
# n = int(input())
# for i in range(len(alist[n])):
#     print(name[alist[n][i]])
# ==========================================================================
# # 문제7. 인접행렬 하드코딩, 특정 노드의 번호 입력, 자식노드의 이름을 출력
# name = 'ABTQVX'
# MAP = [[0, 1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# n = int(input())
# for i in range(6):
#     if MAP[n][i] == 0: continue
#     print(name[i])
# ==========================================================================
# # 문제8. DFS 인접행렬, 탐색 순서를 출력하세요.(노드 번호를 출력)
#
# MAP = [[0, 1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# def dfs(now):
#     print(now, end = ' ')
#     for i in range(6): # 노드의 개수
#         if MAP[now][i] == 0: continue
#         # 재귀호출
#         dfs(i)
# dfs(0)
# ===============================================================================
# 문제9. DFS 인접 리스트(노드 값을 출력)

# name = 'ABTQVX'
#
#
# def dfs(now):
#     print(name[now], end=' ')
#     for i in range(len(m[now])):
#         next = m[now][i]
#         dfs(next)
#
#
# # 인접리스트
# m = [[] for _ in range(6)]
# m[0] = [1, 2, 3]
# m[1] = [4, 5]
# dfs(0)
#===================================================================================
# 문제10. 문제9번 코드 + path 배열 추가(흔적 기록)
# path 배열은 level이 필요하다.

# path = [0] * 10
# path[0] = 'A'
# def dfs(level, now):
#     global path
#     print(chr(ord('A')+now), end = ' ')
#     for i in range(len(m[now])):
#         next = m[now][i]
#         # 'A'에서 이제 'B로 들어간다
#         path[level+1] = chr(ord('A')+next)
#
#         dfs(level+1, next)
#         # 갔다가 돌아오면 지워준다.
#         path[level+1] = 0
#
# m = [[] for _ in range(6)]
# m[0] = [1, 2, 3]
# m[1] = [4, 5]
# # level도 0부터 시작, 현재노드 now
# dfs(0,0)

#=======================================================
#문제 11. 이진트리의 DFS

# bt = [0,'A', 'B', 'T', 'R', 'S', 'V']
# bt += [0] * 100
#
# def dfs(now):
#
#     # 왼쪽으로 8 잘못 탐색, return
#     # 오른쪽으로 9 잘못 탐색 return
#     # 최대 13 잘못 탐색 return
#     if bt[now] == 0:return
#     print(bt[now])
#     # 왼쪽 자식
#     dfs(now * 2)
#
#     dfs(now * 2 + 1)
#
# dfs(1)

#=================================================
# #이진트리의 DFS + path
# bt = [0, 'A', 'B', 'T', 'R', 'S', 'V']
# bt += [0] * 100
# path = [0] * 100
#
# def dfs(level,now):
#
#     # 왼쪽으로 8 잘못 탐색, return
#     # 오른쪽으로 9 잘못 탐색 return
#     # 최대 13 잘못 탐색 return
#     if bt[now] == 0: return
#     print(bt[now])
#     path[level + 1] = bt[now * 2]
#     # 왼쪽 자식
#     dfs(level+1, now * 2)
#     path[level + 1] = 0
#     # 오른쪽 자식
#     path[level + 1] = bt[now * 2 + 1]
#     dfs(level+1, now * 2 + 1)
#     path[level +1] = 0
#
# dfs(1, 1)
#==========================================================
# 인접 리스트 그래프 dfs
#
# used = [0] * 4
# def dfs(now):
#     for i in range(len(m[now])):
#         next = m[now][i]
#         # 방문 했던 곳을 기록
#         used[next] = 1

#==============================================================

#문제 11. 인접리스트, 그래프의 DFS탐색(used 배열 지우지 않기, 모든 노드 1회씩 탐색)
# m = [[] for _ in range(4)]
# m[0] = [1,3]
# m[1] = [2]
# m[2] = [0,3]
# m[3] = [2]
#
# used = [0] * 4
#
# def dfs(now):
#     print(now, end='')
#     for i in range(len(m[now])):
#         next = m[now][i]
#         # used 검사
#         if used[next] == 1: continue
#         used[next] = 1
#         dfs(next)
#
# #시작노드는 방문처리
# used[0] = 1
# dfs(0)
#문제 12. 인접행렬, 그래프의 DFS탐색(used 배열 지우지 않기, 모든 노드 1회씩 탐색)
# def dfs(now):
#     print(now, end='')
#     for i in range(4):
#         if V[i] == 0:
#             if table[now][i] == 1:
#                 V[i] = 1
#                 dfs(i)
#
# table = [[0,1,0,1],
#          [0,0,1,0],
#          [1,0,0,1],
#          [0,0,1,0]]
# V = [0]*4
# V[0] = 1
# dfs(0)
# =========================
# 문제13.

# def dfs(now):
#     global cnt
#     print(now, end='')
#     if now == 2:
#         cnt += 1
#         return
#     for i in range(3):
#         if V[i] == 0:
#             if table[now][i] == 1:
#                 V[i] = 1
#                 dfs(i)
#                 V[i] = 0
#
# table = [[0,1,1],
#          [0,0,1],
#          [1,0,0]]
# V = [0]*3
# V[0] = 1
# cnt = 0
# dfs(0)
# print()
# print(cnt)
#============================================================================
# dfs
# 1. 초기화(인접행렬, used 배열,..)
# 2. 탐색
#     dfs 기본 문제들 --- 1에서 5로 가는데 드는 비용
#                       1에서 5호 가는데 드는 최소비용
#                       1에서 5호 가는 길이 있나요?
#                       1에서 5호 가는 길이  몇개 있나요?

# 가중치 값 == 비용문제
#문제14. 0에서 2로 이동하는데 경로마다 각각 비용이 얼마드냐
# used배열 지우기(모든 경로 탐색), 가중치 인접행렬, 매개변수 sum_v 추가

# MAP = [[0,7,20,8],
#        [0,0,5,0],
#        [15,0,0,0],
#        [0,0,6,0]]
# used = [0] * 4
#
# def dfs(now, sum_v):
#     if now ==2:
#         print(sum_v, end=' ')
#     for i in range(4):
#         if MAP[now][i] == 0:
#             continue
#         if used[i] == 1:
#             continue
#         used[i] =1
#         dfs(i,sum_v+MAP[now][i])
#         used[i] = 0
# used[0] = 1
# dfs(0,0)
#=======================================================================================

# 문제 15-1 모든 노드를 1회 탐색(4출발)

# def dfs1(now):
#     print(now, end=' ')
#     for i in range(6):
#         if table[now][i] == 0: continue
#         if V[i] == 1:continue
#         V[i] = 1
#         dfs1(i)
#
#
# table = [[0,2,6,3,0,0],
#          [2,0,7,4,0,0],
#          [6,7,0,0,0,0],
#          [3,4,2,0,0,0],
#          [0,0,1,0,0,7],
#          [0,0,0,0,0,0]]
#
# V = [0]*6
#
# dfs1(4)


# # 문제 15-2 모든 경로를 1회 탐색(4출발)
def dfs(now):
    print(now, end=' ')
    for i in range(6):
        if table[now][i] == 0: continue
        if V[i] == 1: continue
        V[i] = 1
        dfs(i)
        V[i] = 0


table = [[0,2,6,3,0,0],
         [2,0,7,4,0,0],
         [6,7,0,0,0,0],
         [3,4,2,0,0,0],
         [0,0,1,0,0,7],
         [0,0,0,0,0,0]]

V = [0]*6
V[4] = 1
dfs(4)

# 문제 15-3

def dfs3(now):
    global cnt
    if now == b:
        cnt += 1
        return
    for i in range(6):
        if table[now][i] == 0: continue
        if V[i] == 1: continue
        V[i] = 1
        dfs3(now)
        V[i] = 0


def dfs4(now,sum_v):
    global cnt
    global max_v
    global mins_v

    max_v = max()
    min_v = min()

table = [[0,2,6,3,0,0],
         [2,0,7,4,0,0],
         [6,7,0,0,0,0],
         [3,4,2,0,0,0],
         [0,0,1,0,0,7],
         [0,0,0,0,0,0]]

cnt = 0
V = [0]*6
a,b = map(int,input())