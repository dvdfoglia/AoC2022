import os
d="day6"
dname = os.path.dirname(os.path.abspath(__file__))

def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read()
    input.close()
    return i
l=[]

def findMarker(data,mLenght):
    c=0
    for i in data:
        c+=1
        l.append(i)
        if len(l)==mLenght:
            s=set(l)
            if len(s)==mLenght:
                return c
            else:
                l.remove(l[0])

print(findMarker(read_input(),4))
print(findMarker(read_input(),14))