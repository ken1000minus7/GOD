from itertools import permutations
w=int(input())
d=[]
li=['a','b','c','d','e','f','g','h']
for i in range(w):
    d.append(input())
d=set(d)
m=input().split()
c=1
d1={'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}
for i in permutations(li):
    CHECK=1
    for j in range(8):
        d1[li[j]]=i[j]
    abc=[]
    for k in range(len(m)):
        p=""
        for x in range(len(m[k])):
            p+=d1[m[k][x]]
        if p in d:
            abc.append(p)
        else:
            CHECK=0
            break
    if CHECK==1:
        print(*abc)