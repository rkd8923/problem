N = int(input())

def check(n, l):
    if n==1:
        l[n] = 0
        return 0

    if n%3==0:
        l[n] = min(check(n//3, l)+1, l[n])
    if n%2==0:
        l[n] = min(check(n//2, l)+1, l[n])
    l[n] = min(check(n-1, l)+1, l[n])

    return l[n]

def solution(n):
    l = []
    for x in range(n+1):
        l.append(n+1)
    check(n, l)
    return l[n]
print(solution(N))
