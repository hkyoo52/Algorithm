# 알파벳 개수
# https://www.acmicpc.net/source/share/1a1898996c8542889b32b4c1b2498dd0


word=str(input())

def get_count(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count={alpha : 0 for alpha in alphabet}
    for i in word:
        count[i] +=1
    return count.values()


for i in get_count(word):
    print(i, end=' ')
