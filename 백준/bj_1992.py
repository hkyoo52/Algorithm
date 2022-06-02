# 1992
# 쿼드트리
# https://www.acmicpc.net/problem/1992
# 오류 이유 -> numpy 사용 X

def dfs(arr):
    all_sum=0
    for one_arr in arr:
        all_sum+=sum(one_arr)
    if all_sum==0:
        return 0
    elif all_sum==len(arr)*len(arr):
        return 1
    one = dfs([[i for i in one_arr[:len(one_arr)//2]] for one_arr in arr[:len(arr)//2]])
    two = dfs([[i for i in one_arr[len(one_arr)//2:]] for one_arr in arr[:len(arr)//2]])
    three = dfs([[i for i in one_arr[:len(one_arr)//2]] for one_arr in arr[len(arr)//2:]])
    four = dfs([[i for i in one_arr[len(one_arr)//2:]] for one_arr in arr[len(arr)//2:]])

    anw='('+str(one)+str(two)+str(three)+str(four)+')'
    return anw

arr=['11110000','11110000','00011100','00011100','11110000','11110000','11110011','11110011']
#arr=[]
#n=int(input())
#arr=[sys.stdin.readline().strip() for _ in range(n)]
arr=[[int(j) for j in i] for i in arr]
print(dfs(arr))