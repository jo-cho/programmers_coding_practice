# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(n):
    return n.replace(n[:-4],'*'*len(n[:-4]))

n = "01033334444"