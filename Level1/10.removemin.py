def solution(arr):
    arr.remove(min(arr))
    if len(arr)==0:
        arr.append(-1)
    return arr

# test
arr=[3,1,35,65,66,76,5,2]
arr2 = [3]
print(solution(arr))
print(solution(arr2))