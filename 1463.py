N = int(input())
l = []
def check(n):
    if n==1:
        return 0
    if l[n] > 0:
        return l[n]
    l[n] = check(n-1)+1
    if n%3==0:
        l[n] = min(check(n//3)+1, l[n])
    if n%2==0:
        l[n] = min(check(n//2)+1, l[n])
    return l[n]

def solution(n):
    for x in range(n+1):
        l.append(0)
    check(n)
    return l[n]

print(solution(N))
