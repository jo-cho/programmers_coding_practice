#https://programmers.co.kr/learn/courses/30/lessons/12950
import numpy as np
def solution(arr1, arr2):
    return (np.array(arr1)+np.array(arr2)).tolist()
#test
arr1 = [[3,2],[12,56],[1,3]]
arr2 = [[43,-2],[2,526],[-31,30]]

print(solution(arr1,arr2))