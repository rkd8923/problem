input_words = []
N = int(input())
for x in range(N):
    word = input()
    input_words.append(word)

def solution(words):
    temp = [[] for num in range(51)]
    answer = []
    for x in words:
        if x not in temp[len(x)]:
            temp[len(x)].append(x)
    for x in temp:
        answer += sorted(x)
    return answer

for x in solution(input_words):
    print(x)
