''' Fail(메모리 초과)
N = int(input())

resN = ['1']
for i in range(N-1):
    tmp = resN
    resN = []
    for j in(tmp):
        if(j == '1'):
            resN.append('0')
            resN.append('1')
        else:
            resN.append('1')
            resN.append('0')

res = 0
tmp = '1'
for i in(resN):
    
    if((tmp == '1') and (tmp == '0')):
        res+=1
        
print(res)
'''

res = 0

N = int(input())

for i in range(1, N+1, 1):
    if i == 1:
        result = 0
    elif i%2 == 0:
        result = 2*result+1
    else:
        result = 2*result-1

print(result)