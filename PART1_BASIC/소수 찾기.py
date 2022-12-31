N = int(input())
nums = list(map(int, input().split()))

res = 0

for i in (nums):
    for j in range(2, int(i/2)+2, 1):
        if(j == int(i/2)+1):
            res += 1
        if(i%j == 0):
            break

print(res)

''' # version 2
N = int(input())
nums = list(map(int, input().split()))

res = 0

for i in (nums):
    for j in range(2, int(i/2)+2, 1):
        if(i%j == 0):
            break
        if(j == int(i/2)+1):
            res += 1
    if(i == 2):
        res += 1
print(res)
'''