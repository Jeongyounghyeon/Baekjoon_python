A, B = map(int, input().split())

res = 0
num = 1
k = num
for i in range(1, B+1, 1):
    if(i >= A):
        res += num
    k -= 1
    if(k == 0):
        num += 1
        k = num

print(res)