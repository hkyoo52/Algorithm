# 일곱난쟁이
# https://www.acmicpc.net/problem/2309

from itertools import combinations

heights=[int(input()) for i in range(9)]

def find_7(heights):
    over_height=sum(heights)-100
    for comb in list(combinations(heights, 2)):
        if sum(comb)==over_height:
            not_anw=comb
            break
    anw = [i for i in heights if i not in not_anw]
    anw=sorted(anw)
    return anw

find_7(heights)