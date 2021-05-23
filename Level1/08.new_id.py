# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(id):
    #1
    id = id.lower()
    #2
    exception = list("~!@#$%^&*()=+[{]}:?,<>/")
    for i in exception:
        id = id.replace(i,'')
    #3
    while id.replace('..','.') != id:
        id = id.replace('..','.')
    #4
    id = id.strip('.')
    #5
    if id == '':
        id = 'a'
    #6
    if len(id)>=16:
        id = id[:15].strip('.')
    #7
    while len(id)<=2:
        id = id+id[-1]
    return id

#test
id = "...abcdef@#%WEtwet*aETWEfd_0-3u--1=-ugk.kERthijklWETEWT$%m..n.vlyful..p"
print(solution(id))