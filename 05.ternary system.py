# https://programmers.co.kr/learn/courses/30/lessons/68935

# solution
def solution(n):
    answer = 0
    a=[]
    while n>0:
        n, r = (n//3, n%3)
        a.append(r)
    a.reverse()
    for i in range(0,len(a)):
        answer += a[i]*(3**i)
    return answer

# test
import numpy as np
n = np.random.randint(0,100000, 1)
print(solution(n))
