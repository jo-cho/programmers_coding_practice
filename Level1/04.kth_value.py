# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        command = commands[i]
        value = sorted(array[command[0]-1:command[1]])[command[2]-1]
        answer.append(value)
    return answer

# easy code
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# test
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))
