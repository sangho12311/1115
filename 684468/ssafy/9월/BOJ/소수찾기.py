T = int(input())
num_lst = list(map(int, input().split()))
cnt = 0

for i in num_lst:
    tem = 0
    if i == 2:
        cnt += 1
        continue
    if i != 1:
        for j in range(2, i-1):
            if i % j == 0:
                tem = 1
                break
        if tem == 0:
            cnt += 1

print(cnt)