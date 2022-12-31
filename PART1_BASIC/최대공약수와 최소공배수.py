n1, n2 = map(int, input().split())

min = min(n1, n2)
max = max(n1, n2)

for i in range(min, 0, -1):
    if((min % i == 0) & (max % i == 0)):
        print(i)
        break

i = 1
while(1):
    if((max * i) % min == 0):
        print(max * i)
        break
    i += 1