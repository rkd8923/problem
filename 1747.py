N = input()

def check_palindrome(n_str):
    i = 0
    j = len(n_str)-1
    ret = True
    while i<j:
        if n_str[i] != n_str[j]:
            ret = False
            break
        i += 1
        j -= 1
    return ret

def check_prime(n):
    if n == 1:
        return False
    ret = True
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            ret = False
            break
    return ret
def solution(n):
    n_int = int(n)
    n_str = n
    while True:
        if check_palindrome(n_str):
            if check_prime(n_int):
                break
        n_int += 1
        n_str = str(n_int)
    return n_int
print(solution(N))