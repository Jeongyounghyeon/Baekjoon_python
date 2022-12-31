''' Fail(메모리 초과)
lst = []

N = int(input())
for i in range(N):
    lst += list(map(int, input().split()))
    
lst.sort()

print(lst[-5])
'''

lst = []

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(N-1):
    lst2 = list(map(int, input().split()))
    for j in range(N):
        if(lst2[j] > lst[0]):
            lst[0] = lst2[j]
            lst.sort()

print(lst[0])