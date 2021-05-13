# https://programmers.co.kr/learn/courses/30/lessons/70128

# answer
def solution(a, b):
    list=[]
    for i in range(len(a)):
        list.append(a[i]*b[i])
    answer = sum(list)
    return answer

# test
import numpy as np
n = np.random.randint(1,100)
a = np.random.randint(-1000,1000,n)
b = np.random.randint(-1000,1000,n)

print(solution(a,b))