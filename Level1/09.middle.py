def solution(s):
    if len(s)%2==0:
        out = s[int(len(s)/2)-1]+s[int(len(s)/2)]
    else:
        out = s[int(len(s)/2)]
    return out

print(solution('sbfiweFERQdsaf'))