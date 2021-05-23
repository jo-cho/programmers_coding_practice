# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return day[(sum(days[:a-1])+b-1) % 7]

# test
#if 1st Jan is Friday

M=4
D=21

print(solution(M,D))