# https://programmers.co.kr/learn/courses/30/lessons/12931

def sum_digit(number):
    return sum([int(i) for i in str(number)])

n = 123762
print(sum_digit(n))