_ = int(input())
nums = []
for x in range(_):
    t = int(input())
    nums.append(t)
N = [0, 1, 2, 4, 7, 0, 0, 0, 0, 0, 0, 0]
for x in range(5, 11):
    N[x] = N[x-1] + N[x-2] + N[x-3]
for x in nums:
    print(N[x])

        
