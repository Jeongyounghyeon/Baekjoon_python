list = []
sum = 0

for i in range(9):
    list.append(int(input()))
    sum += list[i]

flag = 0

for i in range(9):
    for j in range(i+1, 9):
        if(sum - list[i] - list[j] == 100):
            rm1, rm2 = list[i], list[j]
            flag = 1
            break
    if(flag == 1):
        break

list.sort()
for k in range(9):
    if((list[k] != rm1) & (list[k] != rm2)):
        print(list[k])