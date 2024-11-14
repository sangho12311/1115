def fuc(text):
    al_lst = []
    tem_result = 0
    for i in range(len(text)):
        if text[i] not in al_lst or text[i-1] == text[i]:
            al_lst.append(text[i])
        else:
            tem_result = 1
            break
    return tem_result


cnt = 0
N = int(input())
for _ in range(N):
    text = list(input())
    if fuc(text) == 0:
        cnt += 1
print(cnt)
