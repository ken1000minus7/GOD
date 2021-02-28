def solve(x,c,t):
    if len(x)<=1:
        return
    p=x[:len(x)//2]
    q=x[(len(x)//2):]
    if len(set(p)&set(q))==0:
        t[0]+=1
    solve(p,c,t)
    solve(q,c,t)
n=int(input())
li=list(map(int,input().split()))
x=[0]
solve(li,0,x)
print(x[0])