# https://programmers.co.kr/learn/courses/30/lessons/12977

# answer
import itertools
def solution(nums):
    c = list(itertools.combinations(nums,3))
    is_prime = []
    for j in range(0,len(c)):
        s = sum(c[j])
        y=[]
        for i in range(2, s):
            y.append((s % i))
        re =1
        for x in y:
            re = re * x
        if re !=0:
            is_prime.append(s)
    answer = len(is_prime)
    return answer

# test
import numpy as np
n = np.random.randint(3,51,1)
nums = np.random.randint(1,1001,n).tolist()

print(solution(nums))