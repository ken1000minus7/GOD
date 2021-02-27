n,m=map(int,input().split())
b=[]
"""
li=[]
d1={} #DICTIONARY FOR STORING INPUT WORDS
d2={} #dictionary for storing len and position of horizontal words 
d3={} #dictionary for storing len and position of vertical words 
for i in range(n):
    p=input()
    d=[]
    a=0
    l=0
    si=0
    ei=0
    for j in range(m):
        d.append(p[j])
        if (p[j]=="b" or p[j]=="r") and a==0:
            a=1 
            l+=1
            si=j
        elif (p[j]=="b" or p[j]=="r") and a==1:
            l+=1 
            ei=j 
            d2[l]=[i,si,ei]
            l=0
        elif a==1:
            l+=1
    b.append(d)
for j in range(m):
    a=0
    l=0
    si=0
    ei=0
    for i in range(n):
        if (b[i][j]=="b" or b[i][j]=="c") and a==0:
            a=1 
            l+=1
            si=i
        elif (b[i][j]=="b" or b[i][j]=="c") and a==1:
            l+=1 
            ei=i 
            d3[l]=[j,si,ei]
            l=0
        elif a==1:
            l+=1
w=int(input())
for i in range(w):
    a=input()
    li.append(a)
    d1[len(a)]=a
row=set() #set of rows filled
column=set() #set of columns filled
sad=0
for i in d1:
    if i in d2:
        r,si,ei=map(int,d2[i])
        for j in range(i):
            sub=b[r][j+si]
            if ((sub!="r" and sub!="c" and sub!="." and sub!="b") or ((j+si) in column and r in row)) and sub!=d1[i][j] and sub!=".":
                print("Invalid")
                #print(sub,r,j+si)
                sad=1 
                break
            else:
                b[r][j+si]=d1[i][j]
        row.add(r)
    elif i in d3:
        c,si,ei=map(int,d3[i])
        for j in range(i):
            sub=b[j+si][c]
            if ((sub!="r" and sub!="c" and sub!="b") or ((j+si) in row and c in column)) and sub!=d1[i][j] and sub!=".":
                print("Invalid")
                #print(sub,j+si,c,d1[i][j])
                sad=1
                break
            else:
                b[j+si][c]=d1[i][j]
        column.add(c)
    else:
        print("Invalid")
        break
    if sad==1:
        break
p=""
if sad==0:
    a=0
    for i in range(n):
        for j in range(m):
            rope=b[i][j]
            if rope==".":
                print("Invalid")
                a=1 
                break
            else:
                p+=rope
        if a==1:
            break
        p+="\n"
    if a==0:
        print(p)

print(b)
print(d1)
print(d2)
print(d3)
print(row,column)
"""
for i in range(n):
    b.append(input().strip())
w = int(input())
words = {}
for i in range(w):
    x = input().strip()
    words[len(x)] = x
horizontal = []
for i in range(n):
    c = 0
    f = False
    for j in range(m):
        if b[i][j] == 'b' or b[i][j] == 'r':
            c += 1
            if not f:
                horizontal.append([i, j])
                f = True
            else:
                horizontal[-1].append(c)
                c = 0
                f = False
        elif f and (b[i][j] == '.' or b[i][j] == 'c'):
            c += 1
vertical = []
for i in range(m):
    c = 0
    f = False
    for j in range(n):
        if b[j][i] == 'b' or b[j][i] == 'c':
            c += 1
            if not f:
                vertical.append([j, i])
                f = True
            else:
                vertical[-1].append(c)
                c = 0
                f = False
        elif f and (b[j][i] == '.' or b[j][i] == 'r'):
            c += 1
resh = []
i = 0
while i < n:
    j = 0
    t = []
    while j < m:
        x = b[i][j]
        if x == '#':
            t.append('#')
            j += 1
        elif x == 'b' or x == 'r':
            for k in horizontal:
                if k[0] == i and k[1] == j:
                    leng = k[2]
                    horizontal.remove([i, j, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        t.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            t.append('-')
            j += 1
    resh.append(''.join(t))
    i += 1
resv = []
i = 0
while i < m:
    j = 0
    t = []
    while j < n:
        x = b[j][i]
        if x == '#':
            t.append('#')
            j += 1
        elif x == 'b' or x == 'c':
            for k in vertical:
                if k[0] == j and k[1] == i:
                    leng = k[2]
                    vertical.remove([j, i, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        t.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            t.append('-')
            j += 1
    resv.append(''.join(t))
    i += 1
trans = []
for i in range(n):
    t = []
    for j in range(m):
        t.append(resv[j][i])
    trans.append(''.join(t))
check=1
res = []
for i in range(n):
    t = []
    for j in range(m):
        hh = resh[i][j]
        vv = trans[i][j]
        if hh == vv:
            t.append(hh)
        elif (hh == '-') and (vv in "qwertyuiopasdfghjklzxcvbnm"):
            t.append(vv)
        elif (vv == '-') and (hh in "qwertyuiopasdfghjklzxcvbnm"):
            t.append(hh)
        else:
            print('Invalid')
            check=0
            break
    if check==1:
        res.append(''.join(t))
    else:
        break
if check==1:
    for i in res:
        print(i)