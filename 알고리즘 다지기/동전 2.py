import sys
input = sys.stdin.readline

n, k = map(int, input().split())

values = set()
for i in range(n):
    values.add(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for i in values:
    for j in range(i, k+1):
        if (dp[j] != 0):
            tmp = dp[j-i]+1
            dp[j] = min(tmp, dp[j])

print(dp[j] if (dp[j] != 10001) else -1)