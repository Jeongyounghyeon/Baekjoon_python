'''fail(런타임 에러)
A, B, N = map(int, input().split())

print(int((A/B)*(10**N))%10)
'''

A, B, N = map(int, input().split())

for i in range(N):
    A = A%B*10

print(int(A/B))