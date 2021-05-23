# https://programmers.co.kr/learn/courses/30/lessons/12906

import pandas as pd
def solution(arr):
    s = pd.Series(arr)
    answer = s.loc[s.diff() != 0].values.tolist()
    return answer