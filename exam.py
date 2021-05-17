# https://programmers.co.kr/learn/courses/30/lessons/42840

import numpy as np
import pandas as pd


def solution(a):
    spj1 = [1, 2, 3, 4, 5]* int(10_000 / 5)
    spj2 = [2, 1, 2, 3, 2, 4, 2, 5] * int(10_000 / 8)
    spj3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(10_000 / 10)

    answered = pd.DataFrame([spj1, spj2, spj3])
    answer_df = pd.DataFrame(np.array(a * 3).reshape(3, len(a)))
    answered_df = answered.iloc[:, :len(a)]
    sums = (answer_df == answered_df).sum(axis=1)
    out = (sums.loc[sums == sums.max()].index + 1).tolist()
    return out

def solution_alt(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result

# test
nprob = np.random.randint(5,10_000,1)
a = np.random.randint(1,5,nprob).tolist()

print("who correct the most : ", solution(a))
print("who correct the most : ", solution_alt(a))


