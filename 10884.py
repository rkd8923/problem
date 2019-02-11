N = int(input())
temp = [0 for x in range(11)]
dp = [list(temp) for x in range(N+1)]

for x in range(1, 10):
    dp[1][x] = 1

for x in range(2, N+1):
    dp[x][0] = dp[x-1][1]
    for y in range(10):
        dp[x][y] = dp[x-1][y-1] + dp[x-1][y+1]
answer = 0
for x in dp[N]:
    answer += x
answer %= 1000000000

print(answer)