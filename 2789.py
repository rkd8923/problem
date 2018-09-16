# ALPHA = [num for num in 'CAMBRIDGE']
input_text = input()
answer = ''
for x in input_text:
    if x not in "CAMBRIDGE":
        answer += x
print(answer)


