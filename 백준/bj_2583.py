# 영역구하기
# https://www.acmicpc.net/problem/2583


from collections import deque

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs(i,j,arr):
    q = deque()
    q.append([i,j])
    arr[i][j]=1
    cnt=1
    while q:
        i,j=q.popleft()
        for num in range(4):
            ni,nj=i+dr[num],j+dc[num]
            if 0<=ni<len(arr) and 0<=nj<len(arr[0]) and arr[ni][nj]==0:
                q.append([ni,nj])
                arr[ni][nj]=1
                cnt+=1
    return cnt

def put_rec(arr,change):
    c1,r1,c2,r2=change
    for r in range(r1,r2):
        for c in range(c1,c2):
            arr[r][c]=1
    return arr



import copy
import sys

M,N,K=map(int,sys.stdin.readline().split())
change_list=[list(map(int,sys.stdin.readline().split())) for _ in range(K)]

a=[[0 for _ in range(N)] for _ in range(M)]

for change in change_list:
    a=put_rec(a,change)

s=copy.deepcopy(a)
anw=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if s[i][j]==0:
            anw.append(bfs(i,j,s))

print(len(anw))
for one_anw in sorted(anw):
    print(one_anw, end=' ')