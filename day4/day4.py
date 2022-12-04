import os
d="day4"
dname = os.path.dirname(os.path.abspath(__file__))

def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i

def solve(data):
    t1=0
    t2=0
    t3=len(data)

    for i in data:
        g=(list(map(int,i.replace("-",",").split(sep=","))))
        if (g[0] <= g[2] and g[1] >= g[3]) or (g[2] <= g[0]) and (g[3] >= g[1]):
            t1+=1
        if (g[0]>g[2]):
            if (g[0]>g[3]):
                t2+=1
        elif g[0]<g[2]:
            if g[1]<g[2]:
                t2+=1
    return t1,t2,t3


res=solve(read_input())
print(res[0])
print(res[2]-res[1])