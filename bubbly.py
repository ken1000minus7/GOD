def bubble(x):
    sw=0
    a=[]
    while True:
        swap=False
        j=1
        for i in range(len(x)-j):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                sw+=1
                a.append(i)
                swap=True
        if not swap:
            return sw,a
        j+=1
n=int(input())
li=list(map(int,input().split()))
sw,a=bubble(li)
print(sw)
print(*a)