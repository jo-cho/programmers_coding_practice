# alternative
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

# test
participant = ["leo", "kiki", "eden"]
completion =["eden", "kiki"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 =["stanko", "ana", "mislav"]

print(solution(participant,completion))
print(solution(participant2,completion2))
