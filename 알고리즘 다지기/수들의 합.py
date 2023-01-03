N = int(input())

res = 1
cnt = 0

while(1):
    cnt += res
    if(cnt > N):
        break
    res += 1
    
print(res - 1)