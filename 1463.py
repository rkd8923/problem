N = int(input())
def check(n):
    l = []
    for x in range(n+1):
        l.append(n+1)
    for x in range(1, n+1):
        if x==1:
            l[x] = 0
        l[x] = min(l[x-1]+1, l[x])
        if x%3==0:
            l[x] = min(l[x//3]+1, l[x])
        if x%2==0:
            l[x] = min(l[x//2]+1, l[x])
    return l
def solution(n):
    lst = check(n)
    return lst[n]

print(solution(N))
