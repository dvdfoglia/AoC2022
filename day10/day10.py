import os
d="day10"
dname = os.path.dirname(os.path.abspath(__file__))
data=[]
res=0
draw=""

def read_input():
    f = dname+"/"+d+".txt"
    with open(f) as file:
        return file.readlines() 

def load_data():
    for i in read_input():
        data.append(i.split())
        if i.split()[0]=="addx":
            data.append(["noop"])
    return data

cycle=1
tmpOdd=0
tmpEven=0
X=1
add2=False
row=0
def noop(c):
    c+=1
    return c

def addx(i,c):
    global tmpEven; global tmpOdd; global add2
    if c % 2 == 1: tmpOdd=int(i)
    else: tmpEven=int(i)
    c+=1
    return c

for i in load_data():
    pos=cycle-(row*40)
    if cycle in range(20,260,40):
        res+=(cycle*X)
    if pos in range(X,X+3): draw+="#"
    else: draw+="."    
    if row<cycle//40: draw+="\n"
    row=cycle//40
    if i[0] == 'noop':
        cycle=(noop(cycle))
    else:
       cycle=(addx(i[1],cycle))
    if cycle % 2 == 1:
        X+=tmpOdd; tmpOdd=0
    else: X+=tmpEven; tmpEven=0
print("Part1", res)


print("\nPart2\n")
print(draw)