# https://programmers.co.kr/learn/courses/30/lessons/12916

# solution
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

# test
s="pPoooyY"
print(solution(s))