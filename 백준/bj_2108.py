# 통계학
# https://www.acmicpc.net/problem/2108

import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

def avg(arr):
    return round(sum(arr)/len(arr))

def center(arr):
    return sorted(arr)[len(arr)//2]

def many(arr):
    num_dict={}
    for i in arr:
        if i in num_dict.keys():
            num_dict[i] +=1
        else:
            num_dict[i] = 1
    num_dict = sorted(num_dict.items())
    num_dict = sorted(num_dict,key=lambda x:x[1],reverse=True)
    if len(num_dict)>1 and num_dict[0][1] == num_dict[1][1]:
        return num_dict[1][0]
    return num_dict[0][0]

def volume(arr):
    return max(arr)-min(arr)


print(avg(arr))
print(center(arr))
print(many(arr))
print(volume(arr))