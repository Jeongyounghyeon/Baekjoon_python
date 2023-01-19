def check_max_color(lst):
    max_color = 1
    for  i in range(N):
        for j in range(N):
            cnt_row_color = 1
            cnt_column_color = 1
            
            for k in range(j + 1, N):
                if lst[i][j] == lst[i][k]:
                    cnt_row_color += 1
                else:
                    cnt_row_color = 1
                max_color = max(max_color, cnt_row_color)
            
            for k in range(i + 1, N):
                if lst[i][j] == lst[k][j]:
                    cnt_column_color += 1
                else:
                    cnt_column_color = 1
                max_color = max(max_color, cnt_column_color)
    return max_color

N = int(input())

lst = []

for i in range(N):
    lst.append(list(input())) 

max_color = 0
for i in range(N-1):
    for j in range(N-1):
        if lst[i][j] != lst[i][j+1]:
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            max_color = max(max_color, check_max_color(lst))
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        if lst[i][j] != lst[i+1][j]:
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            max_color = max(max_color, check_max_color(lst))
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
        
print(max_color)