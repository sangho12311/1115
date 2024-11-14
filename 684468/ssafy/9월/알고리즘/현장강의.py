#병합정렬

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # 배열을 반으로 나누기
    mid = len(arr) // 2
    # 왼쪽 절반 정렬(재귀로)
    left = merge_sort(arr[:mid])
    # 오른쪽 절반 정렬(재귀로)
    right = merge_sort(arr[mid:])
    #정렬된 오른쪽과 오른쪽을 병합 
    return merge(left, right)

def merge(left, right):
    result = [] #정렬된 결과
    i, j = 0, 0 #인덱스 (i : 왼쪽, j: 오른쪽)
    #왼쪽과 오른쪽을 비교하면서 병합(merger)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: # 오른쪽 요소가 더 작다면
            result.append(right[j])
            j += 1
    # while문 끝나고 남은 요소들 extend로 추가 
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = list(map(int,input().split()))
sorted_arr = merge_sort(arr)
print(sorted_arr)

#===========================================
# sort() vs Quick Sort
# 퀵 정렬 스포세스
# 1. 피벗 선택: 배열의 중간 요소
# 2. 분할
# 피벗보다 작은 요소는 left
# 피벗과 같은 요소는 middle
# 피벗보다 큰 요소는 right
# 3. 재귀 + 병합
# left,right를 재귀적정렬 
# left, middle, right순서대로 연결해서 병합

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     #피벗 선택 : 중간요소
#     pivot = arr[len(arr)//2]
#     #피벗보다 작은 요소는 left
#     left = [x for x in arr if x < pivot]
#     # 피벗과 같은 요소는 middle
#     middle = [x for x in arr if x == pivot]
#     # 피벗과 같은 요소는 right
#     right =[x for x in arr if x > pivot]

#     return quick_sort(left) + quick_sort(middle) + quick_sort(right)

# arr = list(map(int,input().split()))
# sorted_arr = quick_sort(arr)
# print(sorted_arr)

#=======================================

# binary_search(이진 탐색)

# 프로세스
# : 정렬된 배열의 mid을 선택
# mid와 target을 비교
# target이 mid보다 작으면 왼쪽 절반만 탐색 (right = mid -1 )
# target이 mid보다 크면 오른쪽 절반 탐색 (left = mid +1)
# 계속 반복 (while문) 값을 찾거나 탐색 범위가 없어질 때까지 (left <= right)

def binary_search(arr, target):
    left = 0
    right = len(arr) -1 
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # target을 찾았다! ---> 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1 #오른쪽 절반 탐색
        else:
            right = mid - 1 #왼쪽 절반 탐색 
    return -1

arr = list(map(int,input().split()))
target = int(input())
result = binary_search(arr, target)

print(f'위치는 {result}')