import os
d="day5"
dname = os.path.dirname(os.path.abspath(__file__))
resultsMoved=""
resultsMoved9001=""

def read_input():
    f = dname+"/"+d+".txt"
    input = open(f,'r')
    i = input.read().splitlines()
    input.close()
    return i
data=read_input()

def parseStacks():
    stacks = {}
    for i in range(1,10):
        stacks['stack' + str(i)] = []
    for i in range(7,-1,-1):
        pos=0
        for x in ([*data[i]]):
            pos+=1
            if (str(x).isspace() or x == "[" or x == "]"):
                pass
            else:
                stacks['stack' + str(int((pos+2)/4))].append(x)
    return stacks

def moveCrates(y):
    for i in range(10,len(data)):
        task=data[i].split()
        q=int(task[1])
        start=task[3]
        end=task[5]
        mv=""
        for x in range(0,q):
            mv=y['stack' + str(start)].pop()
            y['stack' + str(end)].append(mv)
    return y

def moveCrates9001(y):
    for i in range(10,len(data)):
        task=data[i].split()
        q=int(task[1])
        start=task[3]
        end=task[5]
        mv=""
        for x in range(0,q):
            mv+=y['stack' + str(start)].pop()
        for z in range(len(mv)-1,-1,-1):
            y['stack' + str(end)].append(*mv[z])
    return y


stacksMoved=moveCrates(parseStacks())
stacksMoved9001=moveCrates9001(parseStacks())
for i in range(1,10):
    x=stacksMoved
    resultsMoved+=(x['stack' + str(i)].pop())

for i in range(1,10):
    x=stacksMoved9001
    resultsMoved9001+=(x['stack' + str(i)].pop())

print(resultsMoved)
print(resultsMoved9001)