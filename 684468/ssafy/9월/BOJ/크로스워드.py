R, C = map(int, input().split())
table = [list(input())for _ in range(R)]
word = []

for r in range(R):
    tem_lst = []
    for c in range(C):
        if table[r][c] != '#':
                for i in range(C):
                    if c+i<R:
                        if table[r][c + i] == '#':
                            if len(tem_lst) != 1:
                                word.append(''.join(tem_lst))
                                tem_lst = []
                        if c+i < C:
                            tem_lst.append(table[r][c])
print(word)