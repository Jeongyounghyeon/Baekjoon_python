import sys
input = sys.stdin.readline

def noc_coin(value_left, i):
    global noc
    global values
    global n

    if (i >= n):
        return ;
    
    if (i == n-1):
        if (value_left % values[i] == 0):
            noc += 1    
        return ;
        
    for cnt_coin in range(int(value_left / values[i]) + 1):
        if (value_left - (values[i] * cnt_coin) == 0):
            noc += 1
            return ;
        noc_coin(value_left - (values[i] * cnt_coin), i + 1)

n, k = map(int, input().split())

values = []
for i in range(n):
    values.append(int(input()))

noc = 0
noc_coin(k, 0)
print(noc)