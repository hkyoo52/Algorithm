# 단어 정렬
# https://www.acmicpc.net/problem/1181

num=int(input())
words=[]
for _ in range(num):
    words.append(input())
#words=['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']
new_words=[]
for i in words:
    if i not in new_words:
        new_words.append(i)
sorted_words=sorted(new_words)
anw=sorted(sorted_words,key=lambda x: len(x))
for i in anw:
    print(i)