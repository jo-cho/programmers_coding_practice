# https://programmers.co.kr/learn/courses/30/lessons/12915

#my solution
def solution(s, n):
    s = sorted([s[i][n]+s[i] for i in range(len(s))])
    answer = [s[i][1:] for i in range(len(s))]
    return answer

#suggested but for the old one.
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

# test
strings = ["abce", "abcd", "cdx"]
print(solution(strings, 2))