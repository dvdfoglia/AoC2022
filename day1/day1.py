import os
d="day1"
dname = os.path.dirname(os.path.abspath(__file__))

def read_input():
    f=dname+"/"+d+".txt"
    input = open(f,'r')
    i=input.read()
    input.close()
    return i
print(read_input())
#c=0
#for t in read_input():
#    print(t)
#    c=c+1
#    print(c)