import sys
input = sys.stdin.readline

def check_max_color(lst):
    global max_color
    global N

    for i in range(N):
        color = lst[i][0]
        max_now = 0
        for j in range(N):
            if (color==lst[i][j]):
                max_now += 1
            else:
                if (max_now>max_color):
                    max_color = max_now
                max_now = 1
            color = lst[i][j]
        if (max_now>max_color):
            max_color = max_now

    for j in range(N):
        color = lst[0][j]
        max_now = 0
        for i in range(N):
            if (color==lst[i][j]):
                max_now += 1
            else:
                if (max_now>max_color):
                    max_color = max_now
                max_now = 1
            color = lst[i][j]
        if (max_now>max_color):
            max_color = max_now

N = int(input())
lst = [list(input().rstrip()) for i in range(N)]

max_color = 0
for i in range(N):
    for j in range(N):
        if (j<N-1):
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            check_max_color(lst)
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        if (i<N-1):
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            check_max_color(lst)
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]

print(max_color)
