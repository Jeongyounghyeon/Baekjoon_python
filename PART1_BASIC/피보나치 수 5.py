n = int(input())

f1 = 0
f2 = 1

if(n == 0):
    print(f1)
elif(n == 1):
    print(f2)
else:
    for i in range(n-1):
        res = f1 + f2
        f1 = f2
        f2 = res

    print(res)