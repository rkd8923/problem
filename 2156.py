N = int(input())
wine = [0 for x in range(N)]
temp = 0
for x in range(N):
    temp = int(input())
    wine[x] = temp
if N==1:
    print(wine[0])
elif N==2:
    print(wine[0] + wine[1])
elif N==3:
    dp = [0 for x in range(N)]
    dp[0], dp[1] = wine[0], (wine[0]+wine[1])
    case1 = dp[0] + wine[2]
    case2 = wine[1] + wine[2]
    dp[2] = max(case1, case2, dp[1])
    print(dp[2])
else:
    dp = [0 for x in range(N)]
    dp[0], dp[1] = wine[0], (wine[0]+wine[1])
    case1 = dp[0] + wine[2]
    case2 = wine[1] + wine[2]
    dp[2] = max(case1, case2, dp[1])
    for x in range(3, N):
        case1 = dp[x-2] + wine[x]
        case2 = dp[x-3] + wine[x-1] + wine[x]
        case3 = dp[x-1]
        if case1 > case2:
            dp[x] = case1 if (case1 > case3) else case3
        else:
            dp[x] = case2 if (case2 > case3) else case3
    print(dp[N-1])