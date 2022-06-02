import sys
A,B,C = map(int,sys.stdin.readline().split())

time_list=[list(map(int,sys.stdin.readline().split())) for _ in range(3)]
fage=[0,A,B*2,C*3]

max_time=max(map(max,time_list))

know=[0 for _ in range(max_time+1)]

for time in time_list:
    for plus in range(time[0]+1,time[1]+1):
        know[plus]+=1

pay=0
for i in know:
    pay +=fage[i]

print(pay)


