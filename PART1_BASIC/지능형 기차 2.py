max = 0
sum = 0

for i in range(10):
    minus, plus = map(int, input().split())
    sum = sum - minus + plus
    if(sum > max):
        max = sum

print(max)